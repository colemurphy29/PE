#initial brute force solution - took forever (16 seconds)

def divisible(n):
	for x in range(11,21):
		if n%x ==0:
			pass
		else:
			return False
	return True

for x in xrange(9699700, 300000000, 20):
	if divisible(x):
		print x

#solution using lowest common prime factors
print(2*3*2*5*7*2*3*11*13*2*17*19)
