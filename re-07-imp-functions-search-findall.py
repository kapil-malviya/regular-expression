'''
##  search() :

	-> We can use search() function to search the given pattern in the target string.
	-> If the match is available then it returns the Match object which represents 
		first occurrence of the match.
	-> If the match is not available then it returns None




import re

string = input('enter the pattern to search : ')
match = re.search(string, 'abaabaaab')
if match != None :
	print('match is available')
	print('first occurrence with start indes : {} and end index : {}'.format(match.start(), match.end()))
else :
	print('match is not available')
'''


'''
##  findall() :

	-> To find all occurrences of the match.
	-> This function returns a list object which contains all occurrences.



import re

listt = re.findall('[0-9]', 'a7b9K8xx')

print(listt)     #  ['7', '9', '8']


'''


'''
##  finditer() : 

	-> returns the iterator yielding a match object for each match.
	-> on each match object we can call start(), end(), group() function.

'''


import re

#matcher = re.finditer('\d', 'a7bk9z6')     # only digit
matcher = re.finditer('\D', 'a7bk9z6')      # except digits
for match in matcher :
	print('start index : {} end index : {} group : {}'.format(match.start(), match.end(), match.group()))
