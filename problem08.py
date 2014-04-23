largest= 0
string = ""
with open("/Users/colemurphy/PE/largenumgrid.txt", 'r') as infile:
	for line in infile:
		a = line.strip()
		string += a

for x in xrange(0, len(string)):
	b = list(string[x:x+5])
	c = [int(x) for x in b]
	d = reduce(lambda x, y: x*y, c)
	if d > largest:
		largest = d

print largest
		