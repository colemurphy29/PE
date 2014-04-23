from math import sqrt, ceil

#Find the sum of all the primes below two million.

#first pass > brute force 
#took > 1 minute

def is_prime(a):
	for i in xrange(2, int(sqrt(a)+1)):
		if a%i == 0:
			return False
	return True

# total = 2
# for x in xrange(3, 2000000, 2):
# 	if is_prime(x):
# 		total += x

# print total

#second pass > sieve of Eratosthenes (took 1.4 seconds)

def sieve(n):
	nums = [x for x in range(0, n+1)]
	nums[1] = 0
	for y in xrange(2, int(ceil(sqrt(n)))):
		if is_prime(y):
			for z in xrange(2, (n/y)+1):
				nums[y*z] = 0
	return sum(nums)

if __name__ == '__main__':
	print(sieve(2000000))
