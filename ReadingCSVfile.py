# importing csv module
#import matplotlib.pyplot as plt
import csv
import sys

# Show all Arguments in commandline
# $ python main.py Python Command Line Arguments
# Arguments count: 5
# Argument      0: main.py
# Argument      1: Python
# Argument      2: Command
# Argument      3: Line
# Argument      4: Arguments

if __name__ == "__main__":
    print(f"Arguments count: {len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i:>6}: {arg}")

# ===========================================
# =========== initialization data ===========
# ===========================================



# csv file name
#filename = "switchingofftractionmotor.csv"
filename = "Zapis_CAN1.csv"
# initializing the titles and rows list
headlines = []
fields = []
interpretedfields = []
rows = []
interpretedrows = []
interpretedrowsforplot = []

idnodes = []
idnodes_available = []
#
# ========================================================
# =========== initialization and configuration ===========
# ========================================================

# Default config ID = 74 and Byte = 2
# Alternative config ID = 75 and Byte = 2

plot_diagram = False
byte_to_plot = 2
idnodes.append(75)

find_all_ip = True

if len(sys.argv) > 1:
    filename = sys.argv[1]

# ===================================================
# =========== reading node id and process ===========
# ===================================================

RPDO_addr = []
TPDO_addr = []

for id_node in idnodes:
    TPDO_addr.append(384 + 256 * 0 + id_node)
    TPDO_addr.append(384 + 256 * 1 + id_node)
    TPDO_addr.append(384 + 256 * 2 + id_node)
    TPDO_addr.append(384 + 256 * 3 + id_node)
    RPDO_addr.append(512 + 256 * 0 + id_node)
    RPDO_addr.append(512 + 256 * 1 + id_node)
    RPDO_addr.append(512 + 256 * 2 + id_node)
    RPDO_addr.append(512 + 256 * 3 + id_node)

# Display ip nodes before interpretation

print("%10s" % TPDO_addr, end=" "),
print('\n')
print("%10s" % RPDO_addr, end=" "),
print('\n')


# ================================================
# =========== reading csv file section ===========
# ================================================

with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    for i in range(0,6):
        headlines.append(next(csvreader))
        # headlines = next(csvreader)

    # extracting field names through first row
    fields = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

    # get total number of rows
    print("Total no. of rows: %d" % (csvreader.line_num))


# ===================================================
# =========== data interpretation section ===========
# ===================================================

for row in rows:
    # show row to split
    # Display Rows before interpretation
    # print('%10s\n ' % row[0])

    # split row by ; example 00:07:43.914;"24C";"Std";"";"00 00 00 00 00 00 00 00" ->
    # ['00:07:43.909', '"52E"', '"Std"', '""', '"01 57 01 57 00 9C 00 94"'] ->
    # replace "" by empty

    interpretedrows.append(row[0].replace('"', '').split(';'))

    # Display Rows after interpretation
    # print('%10s\n ' % interpretedrows[0])

# additional itnerpretation Headers
interpretedfields = fields[0].replace('"', '').split(';')


# ===================================================
# ===========  query builder data section ===========
# ===================================================

for row in interpretedrows:
    try:
        # print("%10s" % row[1], end=" "),
        # print('\n')

        # check if there is an error. The maximum size is FFFF
        if len(row[1]) < 5:
            tmp_int = int(row[1], base=16)
        else:
            tmp_int = 0
            print("Error on %10s" % row, end=" "),
            print('\n')
        print("query builder datacompare %s == %s" % (tmp_int, RPDO_addr[0]), end=" "),
        if tmp_int == RPDO_addr[0]:
            interpretedrowsforplot.append(row)
            print("%10s" % row, end=" "),
            print('\n')
    except NameError:
        print("%10s" % row, end=" "),


# =========================================
# =========== plot data section ===========
# =========================================

if plot_diagram:

    x = []
    y = []
    """
    for row in interpretedrowsforplot:
        # print("%10s" % row[4].split(' ')[2], end=" ")
        x.append(row[0])
        y.append(int(row[4].split(' ')[byte_to_plot], base=16))

    plt.bar(x, y, color='g', width=0.72, label="CAN-BUS ID: %s Bytes: %s" % (idnodes[0], byte_to_plot))
    plt.xlabel('Date in %s samples' % len(interpretedrowsforplot))
    plt.ylabel('Level')
    plt.title('CAN-BUS chart for 2 bytes short')
    plt.legend()
    plt.show()
    """
# =========================================
# =========== plot data section ===========
# =========================================

if find_all_ip:
    print('\n============================ ID find Section enable ============================\n')
    print('\n============================ TPDO_1 NODEID+0x180 ============================\n')
    tmp_id = 0
    for i in range(0, 127):
        for row in interpretedrows:
            if len(row[1]) < 5:
                tmp_id = int(row[1], base=16)
            else:
                tmp_id = 0
                #print("Error on %10s" % row, end=" "),
                #print('\n')
            # print("Node ID check: %s ==  %s" % (tmp_id, 384 + 256 * 0 + i), end=" ")
            if tmp_id == 384 + 256 * 0 + i:
                idnodes_available.append(i)
                #print("Node ID found: %10s" % row, end=" "),
                #print('\n')
                break
                # brake to next DI

    for id_to_print in idnodes_available:
        print("Node ID found: %s" % id_to_print, end=" "),


# --------------------------------------------------

    print('\n============================ TPDO_2 NODEID+0x280============================\n')
    idnodes_available.clear()
    tmp_id = 0
    for i in range(0, 127):
        for row in interpretedrows:
            if len(row[1]) < 5:
                tmp_id = int(row[1], base=16)
            else:
                tmp_id = 0
                #print("Error on %10s" % row, end=" "),
                #print('\n')
            # print("Node ID check: %s ==  %s" % (tmp_id, 384 + 256 * 0 + i), end=" ")
            if tmp_id == 384 + 256 * 1 + i:
                idnodes_available.append(i)
                #print("Node ID found: %10s" % row, end=" "),
                #print('\n')
                break
                # brake to next DI

    for id_to_print in idnodes_available:
        print("Node ID found: %s" % id_to_print, end=" "),


    print('\n============================ TPDO_3 NODEID+0x380============================\n')

    idnodes_available.clear()
    tmp_id = 0
    for i in range(0, 127):
        for row in interpretedrows:
            if len(row[1]) < 5:
                tmp_id = int(row[1], base=16)
            else:
                tmp_id = 0
                #print("Error on %10s" % row, end=" "),
                #print('\n')
            # print("Node ID check: %s ==  %s" % (tmp_id, 384 + 256 * 0 + i), end=" ")
            if tmp_id == 384 + 256 * 2 + i:
                idnodes_available.append(i)
                #print("Node ID found: %10s" % row, end=" "),
                #print('\n')
                break
                # brake to next DI

    for id_to_print in idnodes_available:
        print("Node ID found: %s" % id_to_print, end=" "),


    print('\n============================ TPDO_4 NODEID+0x480============================\n')
    idnodes_available.clear()
    tmp_id = 0
    for i in range(0, 127):
        for row in interpretedrows:
            if len(row[1]) < 5:
                tmp_id = int(row[1], base=16)
            else:
                tmp_id = 0
                #print("Error on %10s" % row, end=" "),
                #print('\n')
            # print("Node ID check: %s ==  %s" % (tmp_id, 384 + 256 * 0 + i), end=" ")
            if tmp_id == 384 + 256 * 3 + i:
                idnodes_available.append(i)
                #print("Node ID found: %10s" % row, end=" "),
                #print('\n')
                break
                # brake to next DI

    for id_to_print in idnodes_available:
        print("Node ID found: %s" % id_to_print, end=" "),


if find_all_ip:
    print('\n============================ RPDO_1 NODEID+0x200 ============================\n')
    idnodes_available.clear()
    tmp_id = 0
    for i in range(0, 127):
        for row in interpretedrows:
            if len(row[1]) < 5:
                tmp_id = int(row[1], base=16)
            else:
                tmp_id = 0
                #print("Error on %10s" % row, end=" "),
                #print('\n')
            # print("Node ID check: %s ==  %s" % (tmp_id, 384 + 256 * 0 + i), end=" ")
            if tmp_id == 512 + 256 * 0 + i:
                idnodes_available.append(i)
                #print("Node ID found: %10s" % row, end=" "),
                #print('\n')
                break
                # brake to next DI

    for id_to_print in idnodes_available:
        print("Node ID found: %s" % id_to_print, end=" "),




    print('\n============================ RPDO_2 NODEID+0x300 ============================\n')
    idnodes_available.clear()
    tmp_id = 0
    for i in range(0, 127):
        for row in interpretedrows:
            if len(row[1]) < 5:
                tmp_id = int(row[1], base=16)
            else:
                tmp_id = 0
                #print("Error on %10s" % row, end=" "),
                #print('\n')
            # print("Node ID check: %s ==  %s" % (tmp_id, 384 + 256 * 0 + i), end=" ")
            if tmp_id == 512 + 256 * 1 + i:
                idnodes_available.append(i)
                #print("Node ID found: %10s" % row, end=" "),
                #print('\n')
                break
                # brake to next DI

    for id_to_print in idnodes_available:
        print("Node ID found: %s" % id_to_print, end=" "),


    print('\n============================ RPDO_3 NODEID+0x400 ============================\n')
    idnodes_available.clear()
    tmp_id = 0
    for i in range(0, 127):
        for row in interpretedrows:
            if len(row[1]) < 5:
                tmp_id = int(row[1], base=16)
            else:
                tmp_id = 0
                ##print("Error on %10s" % row, end=" "),
                ## print('\n')
            # print("Node ID check: %s ==  %s" % (tmp_id, 384 + 256 * 0 + i), end=" ")
            if tmp_id == 512 + 256 * 2 + i:
                idnodes_available.append(i)
                ##print("Node ID found: %10s" % row, end=" "),
                ##print('\n')
                break
                # brake to next DI

    for id_to_print in idnodes_available:
        print("Node ID found: %s" % id_to_print, end=" "),


    print('\n============================ RPDO_4 NODEID+0x500 ============================\n')
    idnodes_available.clear()
    tmp_id = 0
    for i in range(0, 127):
        for row in interpretedrows:
            if len(row[1]) < 5:
                tmp_id = int(row[1], base=16)
            else:
                tmp_id = 0
                #print("Error on %10s" % row, end=" "),
                #print('\n')
            # print("Node ID check: %s ==  %s" % (tmp_id, 384 + 256 * 0 + i), end=" ")
            if tmp_id == 512 + 256 * 3 + i:
                idnodes_available.append(i)
                #print("Node ID found: %10s" % row, end=" "),
                #print('\n')
                break
                # brake to next DI

    for id_to_print in idnodes_available:
        print("Node ID found: %s" % id_to_print, end=" "),

# ==========================================
# =========== print data section ===========
# ==========================================

print('\n============================ Headlines Section ============================\n')

# printing the field headlines
for headline in headlines:
    print("%10s" % headline, end=" "),
    print('\n')


print('\n============================ Headers Section ============================\n')

# printing the field names
print('Field names are:' + ', '.join(field for field in fields))

print('\n============================ Data Section ============================\n')

# printing first 5 rows
print('\nFirst 5 rows are:\n')
for row in rows[:5]:
    # parsing each column of a row
    for col in row:
        print("%10s" % col, end=" "),
    print('\n')

print('\n============================ Data Section ============================\n')

print("%10s" % interpretedfields, end=" "),
print('\n')


# printing first 5 rows interpretation
print('\nFirst 5 interpretated rows are:\n')
for row in interpretedrows[:5]:
    # parsing each column of a row
    for col in row:
        print("%10s" % col, end=" "),
    print('\n')


for id_to_print in RPDO_addr:
    print("RPDO found: %s" % id_to_print, end=" ")

for id_to_print in TPDO_addr:
    print("UPDO found: %s" % id_to_print, end=" ")