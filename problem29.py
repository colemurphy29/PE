from math import pow

#0.1 seconds

allnums = set()
for x in range(2,101):
	for y in range(2,101):
		allnums.add(int(pow(x,y)))
print(len(allnums))

#or a one liner:
print(len(set([x**y for x in range(2, 101) for y in range(2, 101)])))