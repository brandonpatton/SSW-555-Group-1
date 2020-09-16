from prettytable import PrettyTable

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

inds = []
for x in "bananans":
  inds.append(Individual("1",x,"M","hh",53,True,"dead",["F23"],"NA"))
  
printIndividuals(inds)
printFamily([])
