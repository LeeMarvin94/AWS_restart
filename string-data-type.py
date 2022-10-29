#This python file is for experiencing string data types + } =
myString = "This is a string"
print(myString)
#Let's get the data type of the variable
print(type(myString))
#Let's concatenate the variable using the python buit-in function
print(str(myString) + " is of the type : "+str(type(myString)))
#Let's create two different strings and then concatenate them in one string
string1 = "water"
string2 ="fall"
myString = string1 + string2
print(myString)
#Let's work now with input files
confirm = 'N'
while confirm !='Y':
  name = input("What is your name ? : ")
  animal = input("Your favourite animal's name: ")
  color = input("Your favourite color: ")
  confirm = input("Do you confirm that the given informations+ (Y/N) : ").upper()
print("Your name is {},you like {}s and your favourite coulour is {}".format(name,animal,color))

