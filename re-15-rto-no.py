
## program to check whether given car registration no is valid MP Registration no or not :


import re

string = input("Enter Vehicle Registration Number : ")
match = re.fullmatch("MP[0-6][0-9][A-Z]{2}\d{4}", string)
if match != None :
	print("Valid Vehicle Registration Number");
else :
	print("Invalid Vehicle Registration Number") 
