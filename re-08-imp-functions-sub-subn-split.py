'''
##  sub() :

	-> sub means substitution or replacement
	
	re.sub(regex,replacement,targetstring)

	-> In the target string every matched pattern will be replaced with provided replacement.,



import re
s = re.sub('\d', '-kapil-', 'a7bk9z6')
#s = re.sub('[a-z]', 'x', 'a7bk9z6')
#  wherever digit is there in targetstring replace digit with '-kapil-'

print(s)      


#   a-kapil-bk-kapil-z-kapil-
'''


'''

##  subn() :

	-> It is exactly same as sub except it can also returns the number of replacements.
	-> This function returns a tuple where first element is result string and second 
		element is number of replacements.

	(resultstring, number of replacements)




import re

t = re.subn('[a-z]', '#', 'a7bk9z6')

print(t)                                  #  ('#7##9#6', 4)

print(type(t))       #  <class 'tuple'>

# this returns tuple, & in tuple the first value t[0] is result string and 
#	the second value t[1] is no. of replacement 

print('the result of string : ', t[0])    #  #7##9#6
print('the no. of replacement : ', t[1])  #  4

'''




##  split() :
'''

-> if we want to split the given target string according to a pattern then 
	we should go for split() function.

-> this function returns list of all tokens

'''


import re

# l = re.split('-', '8-18-28-8-38-88-80-98-88')

# print(l)     #  ['8', '18', '28', '8', '38', '88', '80', '98', '88']


l = re.split('\.', 'www.amazon.com')
for t in l :
	print(t)


'''

www
amazon
com                '''