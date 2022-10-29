#This is for file handling experimentation in python programming + } =
import csv
with open('csv_file.csv','r') as File:
 ReadFile = csv.reader(File,delimiter =',')
 for row in ReadFile:
   print(row)
#with open("files/file1.txt","r") as f:
# print(f.read())



