from prettytable import PrettyTable
"""
Author: Alex Saltstein, Daniel Collins, James Surless, Miriam Podkolzin, Kenny Mason, Brandon Patton
Description: This python script reads the specified GEDCOM file that you want to read then outputs in a
  pretty format the individuals and the families
    "--> <input line>" then
    "<-- <level>|<tag>|<valid?> : Y or N|<arguments>"
      <level> is the level of the input line, e.g. 0, 1, 2
      <tag> is the tag associated with the line, e.g. 'INDI', 'FAM', 'DATE', ...
      <valid?> has the value 'Y' if the tag is one of the supported tags or 'N' otherwise.  The set of all valid tags for our project is specified in the Project Overview document.
      <arguments> is the rest of the line beyond the level and tag.
"""
class Individual:
  def __init__(self, iD):
    self.iD = iD
    self.name = ""
    self.gender = ""
    self.birthday = ""
    self.age = ""
    self.alive = "Y"
    self.death = "NA"
    self.child = "NA"
    self.spouse = "NA"

  def addChild(self,child):
    self.child.append(child)

  def toList(self):
    return [self.iD,self.name,self.gender,self.birthday,self.age,self.alive,self.death,self.child if len(self.child) != 0 else "NA",self.spouse]

class Family:
  def __init__(self, iD):
    self.iD = iD
    self.married = ""
    self.divorced = "NA"
    self.husbId = ""
    self.husbName = ""
    self.wifeId = ""
    self.wifeName = ""
    self.children = "NA"

  def addChild(self,child):
    self.children.append(child)
    
  def toList(self):
    return [self.iD,self.married,self.divorced,self.husbId,self.husbName,self.wifeId,self.wifeName,self.children if len(self.children) != 0 else "NA"]
    
def printIndividuals(individuals):
  table = PrettyTable()
  table.field_names = ["ID","Name","Gender","Birthday","Age","Alive","Death","Child","Spouse"]
  for i in individuals:
    table.add_row(i.toList())
  print("Individuals")
  print(table)
  
def printFamily(families):
  table = PrettyTable()
  table.field_names = ["ID","Married","Divorced","Husband ID","Husband Name","Wife ID","Wife Name","Children"]
  for f in families:
    table.add_row(f.toList())
  print("Families")
  print(table)

#beginning of script
validTags = ["INDI","NAME","SEX","BIRT","DEAT","FAMC","FAMS","FAM","MARR","HUSB","WIFE","CHIL","DIV","DATE","HEAD","TRLR","NOTE"]

f = open("my-family.ged", "r")

individuals = []
families = []

def findat(f):
  isInd = False
  found = False
  findingBirt = False
  currI = 0
  for i,line in enumerate(f):
    linelist = line.split(" ")
    i = linelist[1]
    if i[0] == "@":
      if i[1] == "F":
        families.append(Family(i[1:-1]))
        isInd = False
      if i[1] == "I":
        individuals.append(Individual(i[1:-1]))
        isInd = True
      found = True
    elif found:
#      print("isInd: ", isInd)
#      print(linelist)
      tag = linelist[1]
      if isInd:
        #do individual parse
        try:
          validTags.index(tag)
          if tag == "NAME":
            individuals[len(individuals)-1].name = " ".join(linelist[2:])
          if tag == "SEX":
            individuals[len(individuals)-1].gender = linelist[2]
          if tag == "BIRT":
            print("here")
            findingBirt = True

        except:
          pass
#      else:
#        #do fam parse
#        try:
#          tag = validTags.index(list[1])
#        except:
#          #do nothing cause not valid tag
      
        
      
            
findat(f)
#printIndividuals(individuals)
#printFamily(families)
"""
for line in f:
  l = line[:-1] if line.find("\n") != -1 else line
  print("-->",l)
  list = l.split(" ")
  try:
    validTags.index(list[1])
    print("<--", list[0] + "|" + list[1] + "|Y|" + " ".join(list[2:]))
  except:
    try:
      validTags.index(list[2])
      print("<--", list[0] + "|" + list[2] + "|Y|" + list[1])
    except:
      print("<--", list[0] + "|" + list[1] + "|N|" + " ".join(list[2:]))

"""
