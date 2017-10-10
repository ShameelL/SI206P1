import re
file = open('regex_sum_31456.txt','r').read()
num = []
stuff = re.findall('[0-9]+', file)
for x in stuff:
	num.append(int(x))
print("Sum of Numbers:" +str(sum(num)))