from math import factorial

#0.2 seconds

sum = 0
for n in range(23, 101):
	for r in range(0, n+1):
		x = factorial(n)/(factorial(r)*factorial(n-r))
		if x>1000000:
			sum+=1 

print sum

