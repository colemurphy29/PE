

nameset = []
file = open('/Users/colemurphy/PE/names.txt')
for line in file:
	mylist = line.split(',')
	for name in mylist:
		newstring = name.replace("\"", "")
		nameset.append(newstring)

counter = 0 
index = 1
#enumerable not used because apparently it's not usable with such a large list?
#this works though
for name in sorted(nameset):
	namescore = 0
	b = list(name)
	for char in b:
		namescore += ord(char)-64
	counter += namescore * index
	index += 1

print counter