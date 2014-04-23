#number factorials

#0.8 seconds

facs=[1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
digitsum=0
for index in range(3,100000):
	factorialsum = sum([facs[int(a)] for a in str(index)])
	if index == factorialsum:
		digitsum += index
print digitsum
