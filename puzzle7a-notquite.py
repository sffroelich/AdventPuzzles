# python script to solve puzzle 6a:  "Custom Customs"
# ( puzzle 6b just varies variables in same program)
# can be run from within the sff14 python interpretor as:
# exec(open(r"C:\Users\SFF1\OneDrive - HP Inc\Documents\diary\AdventCalendar-Puzzles\puzzle7a.py").read())

# to be run, with the data set "input7.txt"
#################
import re


class Pobj:
    def __init__(self, name):
        self.name = name
        self.childbagsum = 0
        self.numchildren = 0
        self.childbags = {}       # for each child added, key = bagcolor, value = num of bags

    def dump_object_attributes_0(self):
        # simple print of initialized object
        print("\n***dump_obj_0: attributes:")
        print("name: ", self.name)
        print("childbagsum: ", self.childbagsum)
        print("numchildren: ", self.numchildren)
        print("childbags: ", self.childbags)
        print("***dump_obj_0: **end**\n")

    def dump_object_attributes_1(self):
        # simple print of informed (updated with rule info) object
        print("\n***dump_obj_1: attributes:")
        print("name: ", self.name)
        print("childbagsum: ", self.childbagsum)
        print("numchildren: ", self.numchildren)
        print("childbags: ", self.childbags)
        print("***dump_obj_0: **end**\n")

    def parsechildren(self,listline):
        # parent info already removed
        numstr = listline[0]
        if numstr == 'no':
            # no children - data already initialized
            return
        else:               # at least one child - 4 strings; could be more
                listlen = len(listline)
                for i in range(0,listlen,4):         # assume @4, each child
                    num = int(listline[i])
                    cname = listline[i+1] + " " + listline[i + 2]
                    # skip the 'bag[s][,.]'
                    # child info parsed, now update object attributes
                    self.childbagsum += num
                    self.numchildren += 1
                    self.childbags[cname] = num
                    #print("added to parent: ", self.name, "child: ", cname, " of bagcnt: ", num, " for new bagsum of: ", self.childbagsum)
        return


def addancesstor_to_enclist(parentname):   # takes a string
    global enclist
    global found
    # simply fetch the name, and add to global enclist 
    name = parentname
    print("\n*** IN addancesstor_to_enclist; adding to enclist: ", name, "\n")
    found = True
    # blindly add parent to enclist - we'll remove duplicates later
    enclist.append(name)
    return True

def already_in_enclist(parentname):    # takes a string
    # returns True or False
    if (parentname in enclist):        # already there (no need to add again)
        return True
    else:
        return False

def sg_is_child(parentobj):               # takes a object instance
    global found
    # return True or False, if 'shiny gold' is a child
    target = 'shiny gold'
    found = False
    searchparent = parentobj.name
    childcnt = parentobj.numchildren
    print("\n***entered sg_is_child recursion, searching on parent name: ", searchparent, "which has: ", childcnt, "children")
    # get a list of the children, for this parent
        c_dict = parentobj.childbags
        newlist = list()
        for i in c_dict.keys():
            newlist.append(i)
        # now, we have a list of children in newlist
    print("*** the children are: ", newlist, "\n")

    if (parentobj.numchildren == 0):        # no children for this parent, you're done
        section = 'one'                     # logic level of recursion
        found = False
        print("returning from logic level", section, "with found = False")
        return found
    else:
        # check out each child in newlist
        for name in newlist:
            # see if target in newlist
            if (name == target):            # we have a candidate
                section = 'two' 
                found = True
                addancesstor_to_enclist(parentobj.name)
                continue

            else:
               section = 'three'                     # logic level of recursion
               # check out remaining in newlist

                # here's the recursive call
                # convert the string 'name' to the object reference
                n = pnames.index(name)
                sg_is_child(pobj[n])

            if found:
                print("returning from logic level", section, "with found = True")
            else:
                print("returning from logic level", section, "with found = False")
            return found
  

#################
# search pattern for input lines:

f = open(r"C:\Users\SFF1\OneDrive - HP Inc\Documents\diary\AdventCalendar-Puzzles\input7c1.txt", "r")
Lines = f.readlines()

if __name__ == '__main__':

    datalinecount = 0    # count the input lines

    pnames  = []       # a list of the 'parent' names (e.g., "light red"), global
    pnameindex  = 0    # udrf got getting the next name in bagtypenames, global

    pobj = []          # LIST that holds the 'parent' objects (rules from the dataset digestion)
    

 
    for line in Lines:
        line = line.strip('\n')
        if not line:                 # line is empty or EOF - skip
           pass
        else:
            # line-by-line input processing
            datalinecount += 1
            
            inline = re.split("\\s+", line)
            p1 = inline[0]
            p2 = inline[1]
            parentname = p1 + " " + p2      # join the first two words from list
            del inline[0:4]                 # remove the first four strings - no longer needed
            # now split line contains only second half of line:  "no bags..." , or "5 dark olive, etc."
            # add this name to pname list
            pnames.append(parentname)
            # create a class instance for this parent
            parent = Pobj(parentname)

            # diagnostic print:
            #parent.dump_object_attributes_0()

            # fill in the children info
            parent.parsechildren(inline)

            # diagnostic print:
            parent.dump_object_attributes_1()

            # now add this object to the list of parents
            pobj.append(parent)

            pnameindex += 1
            
    print("\ndone reading-processing data - read: ", datalinecount, "lines of input.") 
    print(" read rules for numparents: ", pnameindex) 
    print(" which should agree with length of pnames: ", len(pnames))

    # now, ready to the recursive dive.  for each parent in list (except for 'shiny gold'),
    # get a list of children:
    #                        if no children, return
    #                        if child = shiny gold', then add to enclosure list 'enclist'
    #                        if other children - recursively call this function

    print(" reporting the number in the parent list - pnames:", len(pnames),"\n\n")
    # begin the searches:
    enclist = []       # global, will hold the list of enclosing bag names (answering question 7a)
    found = False      # global, let functions change this
    finishresult = False
    for i in range(len(pnames)):
        parentname = pnames[i]
        if parentname == 'shiny gold':
            pass             # skip the initial dive on target itself
        else:
            parent = pobj[i]
            # call the recursive function - see if true ('shiny gold' is in the children tree, somewhere...)
            foundresult = sg_is_child(parent)
            if foundresult == True:
                print("\nfound parent who encapsulates: ", parentname,"\n")
                print("manually adding parent to enclist")
                enclist.append(parentname)

    # finally, remove any duplicates in enclist
    temp = enclist
    enclist = list(set(temp))
    
    print("recursion dives are done; found this many candidates: ", len(enclist))
    print(" the enclist: \n", enclist)         # comment out if large dataset

    print()
    print("part a complete")