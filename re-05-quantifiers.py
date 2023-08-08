'''

##  Qunatifiers :
	
	We can use quantifiers to specify the number of occurrences to match.,

a  =  Exactly one 'a'
a+  =  Atleast one 'a' 
a*  =  Any number of a's including zero number
a?  =  Atmost one 'a' ie either zero number or one number
a{n}  =  Exactly m number of a's
a{m,n}  =  Minimum m number of a's and Maximum n number of a's


'''


import re

matcher = re.finditer('a{2,3}', 'abaabdaaabaa')

for match in matcher :
	print('start : {},  group : {}'.format(match.start(), match.group()))


'''
a+ : atleast one a

start : 0,  group : a
start : 2,  group : aa
start : 6,  group : aaa
start : 10,  group : aa


a* : any no. of a's including zero also

start : 0,  group : a
start : 1,  group :
start : 2,  group : aa
start : 4,  group :
start : 5,  group :
start : 6,  group : aaa
start : 9,  group :
start : 10,  group : aa
start : 12,  group :


a? : atmost one a  (either one 'a' or zero(except 'a') no. of 'a')

start : 0,  group : a
start : 1,  group :
start : 2,  group : a
start : 3,  group : a
start : 4,  group :
start : 5,  group :
start : 6,  group : a
start : 7,  group : a
start : 8,  group : a
start : 9,  group :
start : 10,  group : a
start : 11,  group : a
start : 12,  group :


a{3} : excactly 3a's : aaa

start : 6,  group : aaa


a{m,n} : minimum 'm' no. and maximum 'n' no.
a{2,3} :

start : 2,  group : aa
start : 6,  group : aaa
start : 10,  group : aa



### Note :

^x  =>  It will check whether target string starts with x or not
x$  =>  It will check whether target string ends with x or not


'''
