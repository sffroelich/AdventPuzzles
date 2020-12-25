# python script to solve puzzle 7b:  "Custom Customs"
# ( puzzle 7a just varies variables in same program)
# can be run from within the sff14 python interpretor as:
# exec(open(r"C:\Users\SFF1\OneDrive - HP Inc\Documents\diary\AdventCalendar-Puzzles\puzzle7a.py").read())

# to be run, with the data set "input7.txt" (or for small test, "input7bx")
#################
import re

enclist = []       # global, will hold the list of enclosing bag names (answering question 7a)
orphans = []       # names that do not appear in any childlist

def getList(dict):
    return dict.keys()

def make_enclist_unique():
    global enclist
    # finally, remove any duplicates in enclist
    temp = enclist
    enclist = list(set(temp))

def find_orphans():
    global orphans
    # deliver the list of names that do not appear in any childlist
    # get complete name list from pnames
    templist = pnames
    for index in range(len(pnames)):
        tname = templist[index]
        # examine each list of childnames - if match, add to orphan list
        # this is an n-squared, intensive search - but makes for quick consult later, on how to escape recursion
        is_orphan = True
        for i in range(len(pnames)):
            obj = pobj[i]
            if (tname in obj.childnames):      # found at least one parent - not an orphan
                is_orphan = False
            if not is_orphan:
                break
        # is is_orphan still true?   then is is one
        if is_orphan:
            orphans.append(tname)
        # get next name to check for orphanage
    # end of searching for parents  - global orphans now a complete list
    #print("\n\n*** find_orphan: found these orphans: \n", orphans)
    return

## obsolete    
#def print_path_to_root(objname):          # takes a string
#    # repeatedly access global dictionary 'childparents' - to assemble a list of names to the ROOT object
#    nextnode = objname        # string name , e.g. pnames[name]
#    mypath = []
#    while (nextnode != 'ROOT'):
#        mypath.append(nextnode)
#        nextnode = childparents[nextnode]
#    # now the list is assembled
#    print("\n my path north is: ", mypath)
#
## obsolete    
#def add_childparent_pair(child, parent):      #takes two strings - self.name of obj
#    global childparents
#    childparents[child] = parent
#    return 

## obsolete    
#def get_my_parents_name(myname):               # looks up, returns string of parent's name
#    return childparents[myname]       

class Pobj:

    def __init__(self, name):    # both 'name' and 'myparent' are strings
        self.name = name
        self.childbagsum = 0
        self.numchildren = 0
        self.childbags = {}                # for each child added, key = bagcolor, value = num of bags
        self.childnames = []             # as long as we're here, put the keys for childbags here, for later

    def dump_object_attributes_0(self):
        # simple print of initialized object
        print("\n***dump_obj_0: attributes:")
        print("name: ", self.name)
        print("childbagsum: ", self.childbagsum)
        print("numchildren: ", self.numchildren)
        print("childbags: ", self.childbags)
        print("childnames: ", self.childnames)
        print("***dump_obj_0: **end**\n")

    def dump_object_attributes_1(self):
        # simple print of informed (updated with rule info) object
        print("\n***dump_obj_1: attributes:")
        print("name: ", self.name)
        print("childbagsum: ", self.childbagsum)
        print("numchildren: ", self.numchildren)
        print("childbags: ", self.childbags)
        print("childnames: ", self.childnames)
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
                    self.childnames.append(cname)
        return

def find_parents(name):              # takes a string
    global enclist

    if name in orphans:              # base condition, exits recursive dive
        return
    else:
        # search all objects, if name matches one of their children, add to the enclist
        found_parent = []

        for index in range(len(pnames)):
            parent = pobj[index].name               # string
            clist = pobj[index].childnames          # list
            if name in clist:
                found_parent.append(parent)

        print("\n*** find_parents - for: ", name, " found these parents: ", found_parent)

        enclist += found_parent             # add found parents to enclist

        make_enclist_unique()               # might optimize here?

        # recursive call - call for each of the found_parents   - terminates when name=name
        for index in range(len(found_parent)):
            fparent = found_parent[index]
            find_parents(fparent)

        return

def count_bags(name, depth, sum):
    # recursively dives into children list, updating sum as it goes
    # let depth = the depth of the recusive call only increment upon entry, report and relay on each call
    #  BASE condition exit: check name obj for "no other bags" --> numchildren ==0

    depth += 1       # increments, since you just arrived.  (report from depth zero is the initial call)
    print("\n*** count_bags depth: ", depth, " called with name: ", name, " and sum: ", sum)

    obj = pobj[pnames.index(name)]
    if obj.numchildren == 0:
        sum += 0     # count just this current, child-less bag
        print("*** count_bags depth: ", depth, " hit BASE CONDITION, about to return sum: ", sum)
        return sum
    else:
        childs = obj.childnames                # list
        # we will sum all the divesums together - one each bagtype
        divesum = 0
        divesums = {}
        for child in childs:
            cmult = obj.childbags[child]        # dictionary lookup
            print("*** count_bags depth: ", depth, "finds child: ", child, " and will mult. by: ", cmult, " the sum returned.")
            divesums[child] = cmult *  (count_bags(child, depth, sum) + 1)    # add a value for this recusive call's sum
        # by here, all the children have been divesum'd
        # now calulate the collected dive sums, and update the runnin sum
        for child in childs:
            divesum += divesums[child]   # sum each of the collected gatype totals
        # now have the divesums for this depth; update sum and return
        sum += divesum         # include current bag interior - yourself
    print("\n*** count_bags depth: ", depth, "RETURNING sum= ", sum)
    return sum

## obsolete    
#def addancesstor_to_enclist(parentname):   # takes a string
#    global enclist
#    global found
#    # simply fetch the name, and add to global enclist 
#    name = parentname
#    print("\n*** IN addancesstor_to_enclist; adding to enclist: ", name, "\n")
#    found = True
#    # blindly add parent to enclist - we'll remove duplicates later
#    enclist.append(name)
#    return True

## obsolete    
#def already_in_enclist(parentname):    # takes a string
#    # returns True or False
#    if (parentname in enclist):        # already there (no need to add again)
#        return True
#    else:
#        return False

# obsolete    
#def sg_is_child(parentobj):               # takes a object instance
#    global found
#    # return True or False, if 'shiny gold' is a child
#    target = 'shiny gold'
#    found = False
#    searchparent = parentobj.name
#    childcnt = parentobj.numchildren
#    print("\n***entered sg_is_child recursion, searching on parent name: ", searchparent, "which has: ", childcnt, "children")
#    # get a list of the children, for this parent
#    c_dict = parentobj.childbags
#    newlist = list()
#    for i in c_dict.keys():
#        newlist.append(i)
#    # now, we have a list of children in newlist
#    print("*** the children are: ", newlist, "\n")
#
#    if (parentobj.numchildren == 0):        # no children for this parent, you're done
#        section = 'one'                     # logic level of recursion
#        print("returning from logic level", section, "\n")
#        return
#    else:
#        # check out each child in newlist
#        for name in newlist:
#            # see if target in newlist
#            if (name == target):            # we have a candidate
#                section = 'two'
#                found = True
#                addancesstor_to_enclist(parentobj.name)
#                continue
#            else:
#                section = 'three'                     # logic level of recursion
#                # check out remaining in newlist
#
#                # here's the recursive call
#                # convert the string 'name' to the object reference
#                n = pnames.index(name)
#                found = sg_is_child(pobj[n])
#
#        if found:
#            print("returning from logic level", section, "with found = True\n")
#        else:
#            print("returning from logic level", section, "with found = False\n")
#        return found
#  

#################

f = open(r"C:\Users\SFF1\OneDrive - HP Inc\Documents\diary\AdventCalendar-Puzzles\input7.txt", "r")
Lines = f.readlines()

if __name__ == '__main__':

    datalinecount = 0    # count the input lines

    pnames  = []       # a list of the 'parent' names (e.g., "light red"), global
    pnameindex  = 0    # udrf got getting the next name in bagtypenames, global

    childparents = {}  # global directory, consisting of childname:parentname key:values, for path info

    pobj = []          # LIST that holds the 'parent' objects (rules from the dataset digestion)
    
    for line in Lines:
        line = line.strip('\n')
        if not line:                 # line is empty or EOF - skip
           pass
        else:
            # line-by-line input processing
            datalinecount += 1
            print(" *** line: ", line)
            inline = re.split("\\s+", line)
            p1 = inline[0]
            p2 = inline[1]
            parentname = p1 + " " + p2      # join the first two words from list
            # add this name to pname list
            pnames.append(parentname)
            del inline[0:4]                 # remove the first four strings - no longer needed
            # now the split line contains only second half of line:  "no bags..." , or "5 dark olive, etc."
 
            # create a class instance for this parent
            parent = Pobj(parentname)

            # diagnostic print:
            #parent.dump_object_attributes_0()

            # fill in the children info
            parent.parsechildren(inline)

            # diagnostic print:
            #parent.dump_object_attributes_1()

            # now add this object to the list of parents
            pobj.append(parent)

            pnameindex += 1
            
    print("\ndone reading-processing data - read: ", datalinecount, "lines of input.") 
    print(" which should agree with length of pnames: ", len(pnames))
    #print(" dump of pnames: ", pnames)

    # begin the searches:
    enclist = []       # global, will hold the list of enclosing bag names (answering question 7a)

    # okay, now for the recursion
    target = 'shiny gold'
    print("\n\n***  ABOUT TO CALL RECURSIVE DIVES! ***")

    # for 7a:  find all the 'orphans' - those nodes that do not appear in any childname lists
    #find_orphans()
    #print("\n\n*** returned from find_orphan: found these orphans: \n", orphans)

    # for 7b: - count the bags within 'shiny gold'
    sumwithin = 0
    depth = 0          # is incremented upone entry of each recusive call.
    sumwithin = count_bags(target,depth,sumwithin)

    print("Counted all the bags for: ", target, "and found it contained: ", sumwithin, "bags")
    
    # for 7a: should have found and recorded all parent/paths of target, recording them in 'enclist' 
    # enclist might contain duplicates
    # finally, remove any duplicates in enclist
    # make_enclist_unique()
    
    #print("recursive dives are done; found this many candidates: ", len(enclist))
    #print(" the enclist: \n", enclist)         # comment out if large dataset

    print()
    #print("part a complete")
    print("part b complete")