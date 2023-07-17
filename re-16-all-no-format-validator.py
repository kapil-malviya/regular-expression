
##  Program to check whether the given mobile no is valid or not (10 or 11 or 12 digit) :

import re

s = input("Enter Mobile Number : ")
m = re.fullmatch("(0|91)?[6-9][0-9]{9}", s)
if m != None :
	print("Valid Mobile Number")
else :
	print("Invalid Mobile Number")