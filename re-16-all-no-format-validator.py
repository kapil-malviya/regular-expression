
##  Program to check whether the given mobile no is valid or not (10 or 11 or 12 digit) :

import re

string = input("Enter Mobile Number : ")
match = re.fullmatch("(0|91)?[6-9][0-9]{9}", string)
if match != None :
	print("Valid Mobile Number")
else :
	print("Invalid Mobile Number")
