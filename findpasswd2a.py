
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


    count = 0
    for i in pswd:
        if i == target:
            count += 1
        else:
            pass
    #print("count= ", count)
    if ( count >= atleast ) and (count <= upto):
        print("Password valid! : ", pswd)
        validcount += 1
    else:
        pass
print()
print("number of valid passwords found to be: ", validcount)