"""
Author: Alex Saltstein
Description: This python script takes as input the name of your GEDCOM file that you want to read then outputs to the console
    "--> <input line>" then
    "<-- <level>|<tag>|<valid?> : Y or N|<arguments>"
      <level> is the level of the input line, e.g. 0, 1, 2
      <tag> is the tag associated with the line, e.g. 'INDI', 'FAM', 'DATE', ...
      <valid?> has the value 'Y' if the tag is one of the supported tags or 'N' otherwise.  The set of all valid tags for our project is specified in the Project Overview document.
      <arguments> is the rest of the line beyond the level and tag.
"""
validTags = ["INDI","NAME","SEX","BIRT","DEAT","FAMC","FAMS","FAM","MARR","HUSB","WIFE","CHIL","DIV","DATE","HEAD","TRLR","NOTE"]

fileName = input("Input the name of the file you want to read:\n")
f = open(fileName, "r")

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
      
