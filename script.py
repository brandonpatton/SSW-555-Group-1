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
  def __init__(self, iD, name, gender, birthday, age, alive, death, child, spouse):
    self.iD = iD
    self.name = name
    self.gender = gender
    self.birthday = birthday
    self.age = age
    self.alive = alive
    self.death = death
    self.child = child
    self.spouse = spouse

  def addChild(self,child):
    self.child.append(child)

  def toList(self):
    return [self.iD,self.name,self.gender,self.birthday,self.age,self.alive,self.death,self.child if len(self.child) != 0 else "NA",self.spouse]

class Family:
  def __init__(self, iD, married, divorced, husbId, husbName, wifeId, wifeName, children):
    self.iD = iD
    self.married = married
    self.divorced = divorced
    self.husbId = husbId
    self.husbName = husbName
    self.wifeId = wifeId
    self.wifeName = wifeName
    self.children = children

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
