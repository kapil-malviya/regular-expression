'''

###  Character classes :

We can use character classes to search a group of characters =>>

-> [abc]  =>  Either a or b or c
-> [^abc] =>  Except a and b and c (remaining)
-> [a-z]  =>  Any Lower case alphabet symbol
-> [A-Z]  =>  Any upper case alphabet symbol
-> [a-zA-Z]  =>  Any alphabet symbol
-> [0-9]  =>  Any digit from 0 to 9
-> [a-zA-Z0-9]  =>  Any alphanumeric character
-> [^a-zA-Z0-9]  =>  Except alphanumeric characters(Special Characters)

'''

import re

matcher = re.finditer('[^a-zA-Z0-9]', 'a7b@k%98zZ')

for m in matcher :
	print('start : {},  end : {},  group : {}'.format(m.start(), m.end(), m.group()))



'''
-> for [abz] =>

start : 0,  end : 1,  group : a
start : 2,  end : 3,  group : b
start : 7,  end : 8,  group : z


-> for [aZ] => 

start : 0,  end : 1,  group : a
start : 8,  end : 9,  group : Z



-> for [^abc] =>

start : 1,  end : 2,  group : 7
start : 3,  end : 4,  group : @
start : 4,  end : 5,  group : k
start : 5,  end : 6,  group : 9
start : 6,  end : 7,  group : 8
start : 7,  end : 8,  group : z
start : 8,  end : 9,  group : Z


-> for [a-zA-Z0-9] =>

start : 0,  end : 1,  group : a
start : 1,  end : 2,  group : 7
start : 2,  end : 3,  group : b
start : 4,  end : 5,  group : k
start : 6,  end : 7,  group : 9
start : 7,  end : 8,  group : 8
start : 8,  end : 9,  group : z
start : 9,  end : 10,  group : Z

-> for [^a-zA-Z0-9] =>

start : 3,  end : 4,  group : @
start : 5,  end : 6,  group : %

'''