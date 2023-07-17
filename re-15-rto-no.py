
## program to check whether given car registration no is valid MP Registration no or not :


import re

s = input("Enter Vehicle Registration Number : ")
m = re.fullmatch("MP[0-6][0-9][A-Z]{2}\d{4}", s)
if m != None :
	print("Valid Vehicle Registration Number");
else :
	print("Invalid Vehicle Registration Number") 