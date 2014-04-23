
#sum all the even fibonacci numbers below 4,000,000

def sumevenfibs(n):
	a, b = 0, 1
	sum = 0
	while b < n:
		a, b = b, a+b 
		if b%2 == 0:
			sum += b
	print sum

if __name__ == '__main__':
	sumevenfibs(4000000)
