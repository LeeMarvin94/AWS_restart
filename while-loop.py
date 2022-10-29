#This python source file is for experimenting python programming + } =
import random
print("welcome to guess the number")
print("The rules are simple, I'll think of a number, and you'll try to guess it")
number = random.randint(1,10)
isGuessRight = False
while isGuessRight != True:
  guess = input("Guess a number between 1 and 10: ")
  if int(guess) == number:
    print("Congratulation you guessed {},that's correct".format(int(guess)))
    isGuessRight = True
  else:
    print("you guessed {} it's not correct try again".format(int(guess)))

print("\nEnd of the program")
    
