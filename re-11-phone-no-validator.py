'''

## Regular Expression to represent all 10 digit mobile numbers :

-> Every number should contains exactly 10 digits
-> The first digit should be 6 or 7 or 8 or 9

[6789][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]
[6789][0-9]{9}  --> taking 0-9, 9 times
[6-9]\d{9}



##  Python program to check whether the given no. is valid mobile no or not :


import re

n = input('enter mobile no. : ')
m = re.fullmatch('[6-9]\d{9}', n)
if m != None :
	print('valid mobile number')
else :
	print('invalid mobile number')


'''

##   numbers.txt

##  python program to extract all mobile no present in numbers.txt where no are 
#	mixed with normal text data :


import re

f1 = open('numbers.txt', 'r')

f2 = open('numbersoutput.txt', 'w')

for line in f1 :
	listt = re.findall('[6-9]\d{9}', line)
	for number in listt :
		f2.write(number+"\n")

print('extracted all mobile numbers into numbersoutput.txt')
f1.close()
f2.close()