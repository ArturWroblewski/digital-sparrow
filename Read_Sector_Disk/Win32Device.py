class Win32Device:
    """
    Class to read and seek a Windows Raw Device IO object without bother.
    It deals with getting the full size, allowing full access to all sectors,
    and alignment with the discs sector size.

    Author: PHOENiX <pragma.exe@gmail.com>
    License: Free, enjoy! This should be a thing open() does by default.
    """

    def __init__(self, target):
        # type: (str) -> None
        self.target = target
        self.sector_size = None
        self.disc_size = None
        self.position = 0

        self.handle = self.get_handle()
        self.geometry = self.get_geometry()

    def __enter__(self):
        return self

    def __exit__(self, *_, **__):
        self.dispose()

    def __len__(self) -> int:
        return self.geometry[-2]

    def dispose(self):
        if self.handle != win32file.INVALID_HANDLE_VALUE:
            win32file.CloseHandle(self.handle)

    def get_target(self):
        # type: () -> str
        """Get UNC target name. Can be `E:` or `PhysicalDriveN`."""
        target = self.target
        if not target.startswith("\\\\.\\"):
            target += rf"\\.\{target}"
        return target

    def get_handle(self):
        # type: () -> int
        """Get a direct handle to the raw UNC target, and unlock its IO capabilities."""
        handle = win32file.CreateFile(
            # https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-createfilea
            self.get_target(),  # target
            win32con.MAXIMUM_ALLOWED,  # desired access
            win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE,  # share mode, write needed
            None,  # security attributes
            win32con.OPEN_EXISTING,  # creation disposition
            win32con.FILE_ATTRIBUTE_NORMAL,  # flags and attributes
            None  # template file
        )
        if handle == win32file.INVALID_HANDLE_VALUE:
            raise RuntimeError("Failed to obtain device handle...")
        # elevate accessible sectors, without this the last 5 sectors (in my case) will not be readable
        win32file.DeviceIoControl(handle, winioctlcon.FSCTL_ALLOW_EXTENDED_DASD_IO, None, None)
        return handle

    def get_geometry(self):
        # type: () -> tuple[int, ...]
        """
        Retrieves information about the physical disk's geometry.
        https://learn.microsoft.com/en-us/windows/win32/api/winioctl/ns-winioctl-disk_geometry_ex

        Returns a tuple of:
            Cylinders-Lo
            Cylinders-Hi
            Media Type
            Tracks Per Cylinder
            Sectors Per Track
            Bytes Per Sector
            Disk Size
            Extra Data
        """
        return struct.unpack("8L", win32file.DeviceIoControl(
            self.handle,  # handle
            winioctlcon.IOCTL_DISK_GET_DRIVE_GEOMETRY_EX,  # ioctl api
            b"",  # in buffer
            32  # out buffer
        ))

    def tell(self):
        # type: () -> int
        """Get current (spoofed) position."""
        return self.position

    def _tell(self):
        # type: () -> int
        """Get current real position."""
        if not self.handle:
            self.handle = self.get_handle()
        return win32file.SetFilePointer(self.handle, 0, win32file.FILE_CURRENT)

    def seek(self, offset, whence=os.SEEK_SET):
        # type: (int, int) -> int
        """Seek at any point in the stream, in an aligned way."""
        if whence == os.SEEK_CUR:
            whence = self.tell()
        elif whence == os.SEEK_END:
            whence = len(self)

        to = whence + offset
        closest = self.align(to)  # get as close as we can while being aligned

        if not self.handle:
            self.handle = self.get_handle()

        pos = win32file.SetFilePointer(self.handle, closest, win32file.FILE_BEGIN)
        if pos != closest:
            raise IOError(f"Seek was not precise...")

        self.position = to  # not actually at this location, read will deal with it
        return to

    def read(self, size=-1):
        # type: (int) -> Optional[bytes]
        """Read any amount of bytes in the stream, in an aligned way."""
        if not self.handle:
            self.handle = self.get_handle()

        sector_size = self.geometry[-3]
        offset = abs(self._tell() - self.tell())

        has_data = b''
        while self._tell() < self.tell() + size:
            res, data = win32file.ReadFile(self.handle, sector_size, None)
            if res != 0:
                raise IOError(f"An error occurred: {res} {data}")
            if len(data) < sector_size:
                raise IOError(f"Read {sector_size - len(data)} less bytes than requested...")
            has_data += data
        # seek to the position wanted + size read, which will then be re-aligned
        self.seek(self.tell() + size)

        return has_data[offset:offset + size]

    def align(self, size, to=None):
        # type: (int, Optional[int]) -> int
        """
        Align size to the closest but floor mod `to` value.
        Examples:
            align(513, to=512)
            >>>512
            align(1023, to=512)
            >>>512
            align(1026, to=512)
            >>>1024
            align(12, to=10)
            >>>10
        """
        if not to:
            to = self.geometry[-3]  # logical bytes per sector value
        return math.floor(size / to) * to