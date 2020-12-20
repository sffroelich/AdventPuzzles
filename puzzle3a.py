#
# python script to solve puzzle 3a:  "Tobaggen Trajectory"
# ( puzzle 3b just varies variables in same program)
# can be run from within the sff14 python interpretor as:
# exec(open(r"C:\Users\SFF1\OneDrive - HP Inc\Documents\diary\AdventCalendar-Puzzles\puzzle3a.py").read())


linelist = [line.rstrip('\n') for line in open(r"C:\Users\SFF1\OneDrive - HP Inc\Documents\diary\AdventCalendar-Puzzles\input3.txt", "r")]

treecnt = 0
right = 1
cx = 0
for i in range(0,322,2):			# input has 323 lines
    cx = (cx + right) % 31
    if ( linelist[i + 2][cx] == '#'):
        treecnt += 1
        pass      #cx = right
    else:
        pass      #cx = right
print("trees encountered: ", treecnt)

