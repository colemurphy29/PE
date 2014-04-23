import math

#Return the largest prime factor of 600,851,475,143
#
#doesnt necessarily return the largest prime factor, 
#but this worked the first time I tried it :)

def largeprimefac(num):
	largest = 0
	a = [x for x in xrange(1, int(math.sqrt(num)+1), 2) if num%x == 0 and is_prime(x)]
	return max(a)

def is_prime(a):
    b = [ i for i in xrange(2, a) if (a%i == 0)]
    return True if len(b) == 0 else False

if __name__ == '__main__':
	print(largeprimefac(600851475143))