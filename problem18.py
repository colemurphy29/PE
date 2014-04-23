lines = []
file = open('/Path/to/file/triangle.txt')
for line in file:
	mylist = line.strip().split(' ')
	mylist = [int(x) for x in mylist]
	lines.append(mylist)

totals = lines[len(lines)-1]
for x in xrange(len(lines)-2, -1, -1):
	temp = []
	for y in xrange(0, len(lines[x])):
		if totals[y] > totals[y+1] or totals[y] == totals[y+1]:
			temp.append(lines[x][y]+totals[y])
		else:
			temp.append(lines[x][y]+totals[y+1])
	totals = temp

print max(totals)






