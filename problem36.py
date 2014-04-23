
#1.3 seconds

counter = 0
for x in range(0,1000000):
	if str(x) == str(x)[::-1]:
		bi = "{0:b}".format(x)
		if bi == bi[::-1]:
			counter += x
print counter

