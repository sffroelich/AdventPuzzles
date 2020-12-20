
linelist = [line.rstrip('') for line in open(r"C:\Users\SFF1\OneDrive - HP Inc\Documents\diary\AdventCalendar-Puzzles\input2.txt", "r")]
validcount = 0

for line in linelist:
    (freq, target, pswd) = line.split()

    freqlist = [ int(x) for x in freq.split('-') ]
    (atleast, upto) = tuple(freqlist)
    #print("atleast= ", atleast, "upto= ", upto)

    target = target.strip(':')
    #print("targetchar: ", target)

    #print("passwd= ", pswd)


    cta = atleast
    ctb = upto

    if (pswd[cta - 1] == target) or (pswd[ctb - 1] == target):
        if (pswd[cta - 1] == target) and (pswd[ctb - 1] == target):
            pass
        else:
            validcount +=1
            print("Password valid! : ", pswd)
    else:
        pass
print()
print("number of valid passwords found to be: ", validcount)