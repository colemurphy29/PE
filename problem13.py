total = 0

#find first 10 integers of the sum of these 100 50-digit numbers
with open("/path/to/file/largesum.txt", 'r') as infile:
	for line in infile:
		a = line.strip()
		total += int(a)

print str(total) [0:10]