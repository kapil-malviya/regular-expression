'''

### Important functions of re module :

-> match()
-> fullmatch()
-> search()
-> findall()
-> finditer()
-> sub()
-> subn()
-> split()
-> compile()                          '''


'''
###  match() :

	-> We can use match function to check the given pattern at beginning 
		of target string.
	-> If the match is available then we will get Match object, 
		otherwise we will get None.                                          '''


'''

import re

string = input('enter pattern to check : ')
matchh = re.match(s, 'abcdefgh')

if matchh != None :
	print('match is available at the begining of the String')
	print('start index {} and end index : {}'.format(m.start(), m.end()))
else :
	print('match is not available at the begining of th index')
'''


'''
###  fullmatch() :

	-> We can use fullmatch() function to match a pattern to all of 
		target string. i.e complete string should be matched according 
		to given pattern.

	-> If complete string matched then this function returns Match object 
		otherwise it returns None 
'''


import re

string = input('enter pattern to check : ')
matchh = re.fullmatch(s, 'abcdefgh ij')

if matchh != None :
	print('full string matched')     # =>> abcdefgh ij
else :
	print('full string not matched')
