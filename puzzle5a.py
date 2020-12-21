# python script to solve puzzle 5a:  "Binary Boarding"
# ( puzzle 5b just varies variables in same program)
# can be run from within the sff14 python interpretor as:
# exec(open(r"C:\Users\SFF1\OneDrive - HP Inc\Documents\diary\AdventCalendar-Puzzles\puzzle5a.py").read())

# to be run, with the data set "input5.txt"

import array


def get_seatid(row, col):
    global topseatid
    seatnr = (row * 8) + col
    if seatnr > topseatid:
        topseatid = seatnr
    return seatnr

def rowcolbyid(seatid):
    row = int(seatid / 8)
    col = seatid - row
    return row, col

def initseats():
    global planeseats         # one dimens. list of 128 integers
    empty = 0
    for row in range(128):
        planeseats.append(row)
        planeseats[row] = empty
    return

def get_row(rstring):
    row = 0
    for p2 in range(6,-1,-1):
        if rstring[p2] == 'B':
            row += (2 ** (6 - p2))
    print("get_row calculated, row = ", row)
    return row                     # int

def get_col(cstring):
    col = 0
    for p2 in range(2,-1,-1):
        if cstring[p2] == 'R':
            col += (2 ** (2 - p2))
    print("get_col calculated, row = ", col)
    return col                     # int

def occupyseat(row, col):
    global planeseats
    global topseatid
    global seatidlist

    seatid = get_seatid(row, col)
    #planeseats[row] += col
    planeseats[row] += 1
    seatidlist.append(seatid)
    print("seat id: ", seatid, "booked.")
    return

def occupy(vectorstring):
    print("booking seat for customer into at: ", vectorstring)
    global planeseats
    global topseatid

    rowstring = vectorstring[0:7]
    colstring = vectorstring[7:10]
    row = get_row(rowstring)
    col = get_col(colstring)
    occupyseat(row, col)
    return

def printrows():
    global planeseats
    global topseatid
    global seatidlist

    print(sorted(seatidlist))

def printmissingseat():
    global planeseats
    global topseatid

    print("top seat booked was: ", topseatid)
    toprow, topcol = rowcolbyid(topseatid)
    print("which means i don't need to go past row: ", toprow, "and seat: ", topcol)

    decode = {
        0: "seat 0 empty",
        1: "seat 1 empty",
        2: "seat 2 empty",
        3: "seat 3 empty",
        4: "seat 4 empty",
        5: "seat 5 empty",
        6: "seat 6 empty",
        7: "seat 7 empty",
    }

    for r in range((topseatid +1)):
        # get the value 0-7 for this row
        cols = planeseats[r]
        if cols == 7 :       #skip - this row is full
            pass
        else:
            print(" row:", r , "has ", decode[cols] )


#################



linelist = []
linelist = [line.rstrip('\n') for line in open(r"C:\Users\SFF1\OneDrive - HP Inc\Documents\diary\AdventCalendar-Puzzles\input5.txt", "r")]

# note - i added a blank line to end of input
if __name__ == '__main__':

    planeseats = []
    initseats()
    print(" planeseats initialized")

    topseatid = 0
    numpassengers = 0
    seatidlist = []

    for line in linelist:
        line = line.split()
        if not line:      # line is empty, or EOF
            print("empty or EOF")
        else:
            # each line is a passenger's seat booking - mark it
            bookingstring = line[0]        #string
            occupy(bookingstring)
            numpassengers += 1
    print("\ndone reading-processing data")
    print("processed data for: ", numpassengers)
    print("highest seat id: ", topseatid)
    print()
    print("start of partb - scanning booked seats...")
    #printmissingseat()
    printrows()
    print("scan complete")


