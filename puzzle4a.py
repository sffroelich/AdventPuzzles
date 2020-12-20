# python script to solve puzzle 4a:  "Passport Processing"
###   ABANDONED - DON'T USE CLASSES - USE 4AA SCRIPT
# ( puzzle 3b just varies variables in same program)
# can be run from within the sff14 python interpretor as:
# exec(open(r"C:\Users\SFF1\OneDrive - HP Inc\Documents\diary\AdventCalendar-Puzzles\puzzle4a.py").read())

class Passport(object):
    _registry = []

    def __init__(self, pid):
        self._registry.append(self)
        self._pid = pid
        self._byr = None

    def get_Byr(self):
        return self._byr

    def set_Byr(self, value):
        self._byr = value

    def get_Iyr(self):
        return self._iyr

    def set_Iyr(self, value):
        self._iyr = value

    def get_Eyr(self):
        return self._eyr

    def set_Eyr(self, value):
        self._eyr = value

    def get_Hgt(self):
        return self._hgt

    def set_Hgt(self, value):
        self._hcl = value

    def get_Hcl(self):
        return self._hgt

    def set_Hcl(self, value):
        self._hcl = value

    def get_Ecl(self):
        return self._egt

    def set_Ecl(self, value):
        self._ecl = value

    def get_Pid(self):
        return self._pid

    def set_Pid(self, value):
        self._pid = value

    def get_Cid(self):
        return self._cid

    def set_Cid(self, value):
        self._cid = value

def splitkeyvalue(mystring):
    # splits apart the attribute string - e.g. "byr:1923"
    (key, value) = mystring.split(':')

def listToString(shortlist, prefix):
    # converts a single-item string in list to just a string, stipping prefix
    str0 = ""
    for charac in shortlist:
        str0 += charac
    return str0.lstrip(prefix)

def addnewobject(pid):
    # creates new object, appends the new pid string to the class registry list - does not fill in the values
    # Passport._registry += [pid]  # this is done automatically, in class __init__ routine
    print("adding new object: ", pid, "has been added to the class registry registry")
    newobj = Passport(pid)
    return newobj
 


linelist = [line.rstrip('\n') for line in open(r"C:\Users\SFF1\OneDrive - HP Inc\Documents\diary\AdventCalendar-Puzzles\input4.txt", "r")]

if __name__ == '__main__':
    currentdata = []
    currentpid  = ""

    for line in linelist:
        line = line.strip()
        if not line:        # line is empty - delimits next passport
            # process all currently accumulated data, since no more data for current passport
            # add the new pid to the class registry (save adding all data until the end of current passport data if found, above)
            newobj = addnewobject(newpid) 
            # for each data item, should strip off the first 4 chars (attribute name - e.g. "byr:" ), and add just the value
            for attrstring in currentdata:
		# strip apart the key:value pair
                (key, value) = attrstring.split(':')

                if key == 'byr':
                    newobj.set_Byr(value)
                if key == 'iyr':
                    newobj.set_Iyr(value)
                if key == 'eyr':
                    newobj.set_Eyr(value)
                if key == 'hgt':
                    newobj.set_Hgt(value)
                if key == 'hcl':
                    newobj.set_Hcl(value)
                if key == 'ecl':
                    newobj.set_Ecl(value)
                if key == 'pid':
                    newobj.set_Pid(value)
                if key == 'cid':
                    newobj.set_Cid(value)


            #print(".... new passport created with these attributes")
            #print("New passport: ", currentdata)
            currentdata = []       # wipe out for next passport
            currentpid  = ""       # wipe out for next passport
            # print(".... passport boundary ....")
            continue
        data = line.split()
        currentdata += data		# append this line's data to current information
        # check data for pid, set to currentpid if found
        pidmatch = [match for match in data if "pid" in match]   # need to strip off "pid:" from front of pid:value string
        if pidmatch:
            print("pid match being added to registry: ", listToString(pidmatch, 'pid:'))
            newpid = listToString(pidmatch, 'pid:')
            currentpid = newpid

print()
numobjs = len(Passport._registry)
print("the number of objects created is:", numobjs)
print()
for attr, value in Passport.__dict__.items():
    print("Attribute: ", str(attr or ""), "Value: ", str(value or ""))
print()

            
