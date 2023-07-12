'''

###  Pre defined Character classes :

-> \s => Space character
-> \S => Any character except space character (other character)
-> \d => Any digit from 0 to 9
-> \D => Any character except digit
-> \w => Any word character [a-zA-Z0-9]
-> \W => Any character except word character (Special Characters)
-> .  => Any character including special characters

'''


import re

matcher = re.finditer('.', 'a7b @k %8Z')

for m in matcher :
	print('start : {},  end : {},  group : {}'.format(m.start(), m.end(), m.group()))


'''
for \s :

start : 3,  end : 4,  group : 
start : 6,  end : 7,  group : 


for \S :

start : 0,  end : 1,  group : a
start : 1,  end : 2,  group : 7
start : 2,  end : 3,  group : b
start : 4,  end : 5,  group : @
start : 5,  end : 6,  group : k
start : 7,  end : 8,  group : %
start : 8,  end : 9,  group : 8
start : 9,  end : 10,  group : Z


for \d : 

start : 1,  end : 2,  group : 7
start : 8,  end : 9,  group : 8


for \D : all except digits

for \w : all except space and special characters

for \W :

start : 3,  end : 4,  group :
start : 4,  end : 5,  group : @
start : 6,  end : 7,  group :
start : 7,  end : 8,  group : %


for . : everything

start : 0,  end : 1,  group : a
start : 1,  end : 2,  group : 7
start : 2,  end : 3,  group : b
start : 3,  end : 4,  group :
start : 4,  end : 5,  group : @
start : 5,  end : 6,  group : k
start : 6,  end : 7,  group :
start : 7,  end : 8,  group : %
start : 8,  end : 9,  group : 8
start : 9,  end : 10,  group : Z

'''