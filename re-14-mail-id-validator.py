
##  program to check whether the given mail id is valid gmail id or not :


import re

s = input('enter email id : ')
m = re.fullmatch('\w[a-zA-Z0-9_.]*@gmail[.]com', s)

# m = re.fullmatch('\w[a-zA-Z0-9_.]*@(gmail|rediffmail)[.]com', s)
# m = re.fullmatch('\w[a-zA-Z0-9_.]*@[a-z0-9]+[.]com', s)   =>> ___@tv9.com
# m = re.fullmatch('\w[a-zA-Z0-9_.]*@[a-z0-9]+[.][a-z]+', s)   =>> ___@tv9.net


if m != None :
	print('Valid')
else :
	print('Invalid')