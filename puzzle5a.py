# python script to solve puzzle 5a:  "Binary Boarding"
# ( puzzle 5b just varies variables in same program)
# can be run from within the sff14 python interpretor as:
# exec(open(r"C:\Users\SFF1\OneDrive - HP Inc\Documents\diary\AdventCalendar-Puzzles\puzzle5a.py").read())

# to be run, with the data set "input5.txt"

import array


def get_seatid(row, col):
    seatnr = (row * 8) + col
    if seatnr > topseatid:
        topseatid = seatnr
    return seatnr

def rowcolbyid(seatid):
    row = seatid / 8
    col = seatid - row
    return row, col

def initseats(parray):
    emptycol = [0,0,0,0,0,0,0]
    for row in range(127):
        parray.insert(row, emptycol)
    return parray

def get_row(rstring):
    row = 0
    for p2 in range(7, -1, -1):
        if rstring[p2] == 'B':
            row += 2 ** p2
    return row                     # int

def get_col(cstring):
    col = 0
    for p2 in range(3, -1, -1):
        if cstring[p2] == 'R':
            col += 2 ** p2
    return col                     # int

def occupy(parray, vectorstring):
    row = 0
    col = 0
    seatid = 0
    rowstring = vectorstring[0:7]
    colstring = vectorstring[7:10]
    row = get_row(rowstring)
    col = get_col(colstring)
    seatid = get_seatid(row, col)
    return row, col, seatid


#################

planeseats = []
topseatid = 0

linelist = [line.rstrip('\n') for line in open(r"C:\Users\SFF1\OneDrive - HP Inc\Documents\diary\AdventCalendar-Puzzles\input5.txt", "r")]

# note - i added a blank line to end of input
if __name__ == '__main__':
    print("hello, world")
    pass
