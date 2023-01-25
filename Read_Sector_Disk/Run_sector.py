
handle = win32file.CreateFile(
    r"\\.\D:",
    win32con.MAXIMUM_ALLOWED,
    win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE,
    None,
    win32con.OPEN_EXISTING,
    win32con.FILE_ATTRIBUTE_NORMAL,
    None
)
if handle == win32file.INVALID_HANDLE_VALUE:
    raise RuntimeError("Failed to obtain device handle...")
win32file.DeviceIoControl(handle, winioctlcon.FSCTL_ALLOW_EXTENDED_DASD_IO, None, None)