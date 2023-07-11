import re

pattern = re.compile('ba')
matcher = pattern.finditer('abaababa')
count = 0
for m in matcher :
	count+=1
	print('start : {}, end : {}, group : {}'.format(m.start(), m.end(), m.group()))

print('total no. of occurrences : ', count)


'''  for : ab ;
start : 0, end : 2, group : ab
start : 3, end : 5, group : ab
start : 5, end : 7, group : ab
total no. of occurrences :  3              '''


''' for : ba ;
start : 1, end : 3, group : ba
start : 4, end : 6, group : ba
start : 6, end : 8, group : ba
total no. of occurrences :  3              '''