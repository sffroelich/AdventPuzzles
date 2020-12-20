# python script to solve puzzle 4b:  "Passport Processing"
# ( puzzle 3b just varies variables in same program)
# can be run from within the sff14 python interpretor as:
# exec(open(r"C:\Users\SFF1\OneDrive - HP Inc\Documents\diary\AdventCalendar-Puzzles\puzzle4b.py").read())

# found 194 valid passports, with the data set "input4.txt"
import re

## for part two - restrinctions on values of various key:values
#byr (Birth Year) - four digits; at least 1920 and at most 2002.
#iyr (Issue Year) - four digits; at least 2010 and at most 2020.
#eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
#hgt (Height) - a number followed by either cm or in:
#     If cm, the number must be at least 150 and at most 193.
#     If in, the number must be at least 59 and at most 76.
#hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
#ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
#pid (Passport ID) - a nine-digit number, including leading zeroes.
#cid (Country ID) - ignored, missing or not.     my logic handles this already
#
#########  so, create these boolean functions
def Byr(pdict):
    #byr (Birth Year) - four digits; at least 1920 and at most 2002.
    birthyear = int(pdict.get('byr'))
    if (birthyear >=1920) and (birthyear <= 2002):
        pass     # for debugging, else return 1
        #print("check for valid birth year: ", birthyear, "is good")
        return 1
    else:
        print("check for valid birth year: ", birthyear, "is bad")
        return 0

def Iyr(pdict):
    #iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    issueyear = int(pdict.get('iyr'))
    if (issueyear >=2010) and (issueyear <= 2020):
        pass     # for debugging, else return 1
        #print("check for valid issue year: ", issueyear, "is good")
        return 1
    else:
        print("check for valid issue year: ", issueyear, "is bad")
        return 0

def Eyr(pdict):
    #eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    expireyear = int(pdict.get('eyr'))
    if (expireyear >=2020) and (expireyear <= 2030):
        pass     # for debugging, else return 1
        #print("check for valid expire year: ", expireyear, "is good")
        return 1
    else:
        print("check for valid expire year: ", expireyear, "is bad")
        return 0

def Hgt(pdict):
#hgt (Height) - a number followed by either cm or in:
#     If cm, the number must be at least 150 and at most 193.
#     If in, the number must be at least 59 and at most 76.
    #RE = "^(\d{3}cm)|(\d{2}in)$"
    hgt = str(pdict.get('hgt'))
    if (re.match(r"(\d{3}cm)|(\d{2}in)$",hgt)):
        pass     # for debugging, else return 1
        if (re.match(r"(\d{3}cm)$",hgt)):

            cmlist = re.findall('\d{3}',hgt)
            cm = int(cmlist[0])

            if (cm >= 150) and (cm <= 193):
                #print(" centimeter height: ", cm, "is good")
                return 1
            else:
                print(" centimeter height: ", cm, " of string: ", hgt,  "is bad")
                return 0

        if (re.match(r"(\d{2}in)$",hgt)):

            inchlist = re.findall('\d{2}',hgt)
            inch = int(inchlist[0])

            if (inch >= 59) and (inch <= 76):
                #print(" inches height: ", inch, "is good")
                return 1
            else:
                print(" inches height: ", inch,  " of string: ", hgt,  "is bad")
                return 0

        #print("check for valid height: ", hgt, "is good")
        return 1
    else:
        print("check for valid height: ", hgt, "is bad")
        return 0   

def Hcl(pdict):
    #hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    #RE = "^#[0-9a-f]{6}$"
    hairc = str(pdict.get('hcl'))
    if (re.match(r"#[0-9a-f]{6}$",hairc)):
        pass     # for debugging, else return 1
        #print("check for valid hair color: ", hairc, "is good")
        return 1
    else:
        print("check for valid hair color: ", hairc, "is bad")
        return 0

def Ecl(pdict):
    #ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    #RE = "^(amb)|(blu)|(brn)|(gry)|(hzl)|(oth)$"
    eyec = str(pdict.get('ecl'))
    if (re.match(r"(amb)|(blu)|(brn)|(gry)|(grn)|(hzl)|(oth)$",eyec)):
        pass     # for debugging, else return 1
        #print("check for valid eye color: ", eyec, "is good")
        return 1
    else:
        print("check for valid eye color: ", eyec, "is bad")
        return 0   

def Pid(pdict):
    #pid (Passport ID) - a nine-digit number, including leading zeroes.
    #RE = "^[0-9]{9}$"
    pid = str(pdict.get('pid'))
    if (re.match(r"[0-9]{9}$",pid)):
        pass     # for debugging, else return 1
        #print("check for valid pid: ", pid, "is good")
        return 1
    else:
        print("check for valid pid: ", pid, "is bad")
        return 0

def countifvalid(pdict):
    # if it passes all the checks, then return a 1 - if not, a zero 
    # will only be called if valid candidate (if missing 'cid' - that's ok - ignored)
    # therfore need to pass all 7 tests
    numok = 0
    numok += Byr(pdict)
    numok += Iyr(pdict)
    numok += Eyr(pdict)
    numok += Hgt(pdict)
    numok += Hcl(pdict)
    numok += Ecl(pdict)
    numok += Pid(pdict)
    if numok == 7:
        return 1
    else:
        return 0

##################


linelist = [line.rstrip('\n') for line in open(r"C:\Users\SFF1\OneDrive - HP Inc\Documents\diary\AdventCalendar-Puzzles\input4.txt", "r")]
# note - i added a blank line to end of input
if __name__ == '__main__':
    pports = []       # list of passport pid's - strings
    passports = []    # a list of dictionaries - each dictionary, a passport (in random order!)
    
    currentdata = {}
    currentpid  = ""

    for line in linelist:
        #print("processing line: ", line)
        line = line.split()
        if not line:        # line is empty - delimits next passport
            # process all currently accumulated data, since no more data for current passport
            # end of current passport data, so add current pid to passport array
            pports.append(currentpid)       # add current pid to pidlist
            passports.append(currentdata)   # add current pid's dictionary
            #print("appended pid:", currentpid)
            #
            currentdata = {}      #wipe out for next passport
            #currentpid = ""      #wipe out for next passport
            #print(".... passport boundary ....")
        else:
            # process the line - key:value pairs
            for attrstring in line:
                #print("working on attrstring: ", attrstring)
		# strip apart the key:value pair
                (key, value) = attrstring.split(':')        # key='attrname', value='1235', e.g.
                if key == 'pid':
                    currentpid = value
                # add the current attrstring to the current dictionary
                currentdata[key] = value
        # finished processing this line

    # finished processing data
    numpassports = len(pports)
    print("processed this many passports:", numpassports)

    # now iterate over the passports, and count the 'valid' passports that have required nr of fields
    numvalid = 0
    pnum = 0
    for passport in passports:        # passport is a dictionary
        pnum += 1
        #print("passport number: ", pnum, "has ",len(passport), "items")
        plen = len(passport)
        if plen >= 7:
            if plen == 8:    
                numvalid += countifvalid(passport)
            else:
                # is 'cid' present?  optional
                if 'cid' in passport:
                    pass      # MUST be missing other critical key!
                else:                  
                    numvalid += countifvalid(passport)
        # get next passport - bottom of for checking
    # finished counting valid passports
    print("\nThe number of valid passports is: ", numvalid)

