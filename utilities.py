import calendar
from datetime import datetime
import dateutil.relativedelta

def findParentDeath(indi_iD, listOfIndis):
    '''Loops through list of individuals, finds a specific parent's death date, and returns that information'''
    for i in listOfIndis:
        if indi_iD == i.iD:
            if not i.alive:
                return i.death

def findChildBday(child_iD, listOfIndis):
    '''Loops through list of individuals, finds a specific individuals birth date, and returns that information'''
    for i in listOfIndis:
        if child_iD == i.iD:
            if i.alive:
                return i.birthday

def birthBeforeDeathOfParents(listOfFamilies, listOfIndividuals):
    '''Families have a list of children. The list contains the individual IDs for each child
        For example: Family ID: F1 has Children with IDs: ['I1', 'I4', 'I5']
        MORE INFO'''
    output = []
    KEY_WORD = "ERROR: INDIVIDUALS: US09: "
    for f in listOfFamilies:
        listOfChildren = f.children     #List of strings of individual ids of children
        husband = f.husbId              #string of husband's individual id
        wife = f.wifeId                 #string of wife's individual id
        husbandDeath = findParentDeath(husband, listOfIndividuals)     #store husband's death date if applicable
        wifeDeath = findParentDeath(wife, listOfIndividuals)           #store wife's death date if applicable

        for c in listOfChildren:                                       #loop through list of children IDs
            childBirthday = findChildBday(c, listOfIndividuals)        #get child's birthday
            cBDatetime = datetime.strptime(childBirthday, "%d %b %Y")
            if wifeDeath is not None:                                   #check if wifeDeath exists
                wDDatetime = datetime.strptime(wifeDeath, "%d %b %Y")   #convert wife's death to datetime object from string
                if cBDatetime > wDDatetime:                             #if Mother's death date is before birth of child, not possible
                    print("ANOMOLY: Mother's death cannot come before Child's birth")
                    output.append(c)        #appends problematic child id to output
            if husbandDeath is not None:                                                           #check if husbandDeath exists
                hDDatetime = datetime.strptime(husbandDeath, "%d %b %Y")                           #convert husband's death to datetime object from string
                if (cBDatetime - dateutil.relativedelta.relativedelta(months=9)) > hDDatetime:     #left operand is conception date. if that's greater than the father's death date, that is impossible
                    print("ANOMOLY: Father's death cannot come after 9 months before Child's birth (Child's conception date)")
                    output.append(c)        #appends problematic child id to output