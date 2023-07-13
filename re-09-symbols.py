'''
##   ^ symbol   ==>>

-> we can use ^ symbol to check whether the given target string starts with our 
	provided pattern or not.

Eg.  res = re.search('^Learn', s)
	
	-> if the target string starts with 'Learn', then it will return match object,
		otherwise it'll return None



import re

s = 'Learning Devops is very easy'
res = re.search('^Learnin', s)
if res != None :
	print('target string starts with Learn')
else :
	print('target string does not starts with Learn')


# output ==>> target string starts with Learn




##   $ symbol  ==>>

-> we can use $ symbol to check whether the given target string ends with our provided
	pattern or not

Eg.  res = re.search('easy$', s)

-> if the target string ends with easy, then it will return match object,
	otherwise it will return None

'''


import re 

s = 'Learning Devops is very easy'
#res = re.search(' easy$', s)
res = re.search("EaSy$", s, re.IGNORECASE) 
if res != None :
	print('target string ends with easy')
else :
	print('does not ends with easy')


# output ==>  target string ends with easy