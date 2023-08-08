
##  program to check whether the given mail id is valid gmail id or not :


import re

string = input('enter email id : ')
match = re.fullmatch('\w[a-zA-Z0-9_.]*@gmail[.]com', string)

# match = re.fullmatch('\w[a-zA-Z0-9_.]*@(gmail|rediffmail)[.]com', string)
# match = re.fullmatch('\w[a-zA-Z0-9_.]*@[a-z0-9]+[.]com', string)   =>> ___@tv9.com
# match = re.fullmatch('\w[a-zA-Z0-9_.]*@[a-z0-9]+[.][a-z]+', string)   =>> ___@tv9.net


if match != None :
	print('Valid')
else :
	print('Invalid')
