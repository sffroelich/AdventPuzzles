# python script to solve puzzle 6a:  "Custom Customs"
# ( puzzle 6b just varies variables in same program)
# can be run from within the sff14 python interpretor as:
# exec(open(r"C:\Users\SFF1\OneDrive - HP Inc\Documents\diary\AdventCalendar-Puzzles\puzzle6a.py").read())

# to be run, with the data set "input6.txt"
#################
import array
from collections import Counter

def common(str1, str2):
    # assume str1 = currentstr 
    # if str1 is empty (first add), then return string 2, sorted - later
    if ((len(str1) == 0) and (numpepingroup == 0)):
        return str2

    dict1 = Counter(str1)
    dict2 = Counter(str2)
    # get intersection of the dicionaries
    commonDict = dict1 & dict2

    if len(commonDict) == 0:
        empty = ""

        return empty
    # get a list of the common elements
    commonChars = list(commonDict.elements())
    #sort list in ascending order
    commonChars = sorted(commonChars)
    # return sorted string from the list elements in commonChars
    return ''.join(commonChars)

def unamiyesses(persstring):
    global curgroupstr
    global curgroupyescnt
    global numpepingroup

    if numpepingroup == 1:      # you're done - unanimous!
        curgroupstr = persstring
        curgroupyescnt = len(persstring)
        return

    unistr = common(curgroupstr, persstring)
    curgroupstr = unistr
    if curgroupstr == "":
        curgroupyescnt = 0
    else:
        curgroupyescnt = len(unistr)
    
    print("addedintersected: ", persstring, ", and now curgroupstr = ", curgroupstr)
    print("curgroupyescnt = ", curgroupyescnt)
    return

def addyesses(persstring):
    global curgroupstr
    global curgroupyescnt

    tmpstr = ''.join(set(persstring))

    curgroupstr += tmpstr

    tmpstr = ''.join(set(curgroupstr))

    tmpstr  = ''.join(sorted(tmpstr))

    curgroupstr = tmpstr
    curgroupyescnt = len(curgroupstr)

    return
 
#################

f = open(r"C:\Users\SFF1\OneDrive - HP Inc\Documents\diary\AdventCalendar-Puzzles\input6.txt", "r")
Lines = f.readlines()

if __name__ == '__main__':


    groupcnt = 0       # counter, how many groups
    curgroupstr = ''   # collects string of up to 26chars for any yes from currentgoup.
    curgroupyescnt = 0
    sumyesses = 0
    numpepingroup = 0   # number of people in group - increase by one each line of data

    for line in Lines:
        line = line.strip('\n')
        if not line:      # line is empty, delimiting the last group's input
            # for the current group's string - which is kept uniq - count the yes's
            if curgroupstr:             # check for null string
                pass
            else:
                curgroupyescnt = 0
            # add into the running total
            sumyesses += curgroupyescnt
           # increment group counter
            groupcnt += 1

            # reset curgroupyescnt and curgroupstr for next group
            curgroupyescnt = 0
            numpepingroup = 0
            curgroupstr = ''
        else:
            # keep adding group input: get string, add to current string, uniq the current string
            personinputstr = line        # get string
            numpepingroup += 1
            #addyesses(personinputstr)
            unamiyesses(personinputstr)

    if curgroupstr:             # check for null string
        pass
    else:
        curgroupyescnt = 0

    #curgroupyescnt = len(curgroupstr)
    sumyesses += curgroupyescnt
    groupcnt += 1
    print("end of group:", groupcnt, ", which had: ", curgroupyescnt, " yesses. sum of all group yeseses = ", sumyesses, "\n")   
    print("\ndone reading-processing data")
    print("processed data for: ", groupcnt, " groups.")
    print("all group yes count = ", sumyesses)
    print()
    print("part b complete")
