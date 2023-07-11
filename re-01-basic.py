'''

###  Regular Expressions

-> If we want to represent a group of Strings according to a particular 
	format/pattern then we should go for Regular Expressions.

	i.e Regualr Expressions is a declarative mechanism to represent a group 
		of Strings accroding to particular format/pattern.

	- We can write a regular expression to represent all mobile numbers
	- We can write a regular expression to represent all mail ids

-> The main important application areas of Regular Expressions are :

	- To develop validation frameworks/validation logic
	- To develop Pattern matching applications (ctrl-f in windows, grep in UNIX etc)
	- To develop Translators like compilers, interpreters etc
	- To develop digital circuits
	- To develop communication protocols like TCP/IP, UDP etc.

-> We can develop Regular Expression Based applications by using python module : re
	This module contains several inbuilt functions to use Regular Expressions 
	very easily in our applications.


# compile()

-> re module contains compile() function to compile a pattern into RegexObject.
	pattern = re.compile("ab")

# finditer() :

-> Returns an Iterator object which yields Match object for every Match
	matcher = pattern.finditer("abaababa")

: On Match object we can call the following methods :
-> start() = Returns start index of the match
-> end()   = Returns end+1 index of the match
-> group() = Returns the matched string (item)

'''



import re

pattern = re.compile('ab')
matcher = pattern.finditer('abaababa')
count = 0
for match in matcher :
	count+=1
	print('match is availale at start index : ', match.start())

print('total no. of occurrences : ', count)

'''
We can pass pattern directly as argument to finditer() function =>

	matcher = re.finditer("ab", "abaababa")                                 '''

