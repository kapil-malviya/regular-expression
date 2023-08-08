'''
# write a regular expression to represent all Anaconda language identifiers :

=> Rules :

-> allowed characters : 
	- alphabets
	- digits
	- #
-> the first character should be lower case alphabet symbol from a to k
-> the second character should be any digit divisible by 3
-> the length of identifier should be atleast 2

[0369] -> either 0 or 3 or 6 or 9

=> [a-k][0369] ______

'''


import re 

string = input('enter identifier to validate : ')

match = re.fullmatch('[a-k][0369][a-zA-Z0-9#]*', s)

if match != None :
	print(s, 'is valid Anaconda identifier')
else :
	print(s, 'is not a valid Anaconda identifier')

