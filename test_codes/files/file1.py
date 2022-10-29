#This simple python file is for experiencing different effects of a mixed type list + } =
#myMixedList = ["amour",12,23.4,"34",True]
#for item in myMixedList:
#  print(item)

myDictionary = {
    "cawer":"software engineering",
    "victoire":"agro-industrie",
    "watsapper":"genie-industriel",
    "audrey":"lycee technique",
    "nanick":"infirmerie",
    "dax-man":"genie-civil",
    "Lee Marvin":"software engineering"}
#let's display all the items that holds the dictionary
count =1
for key,value in myDictionary.items():
  print("{} - {} : {}\n".format(count,key,value))
  count += 1

