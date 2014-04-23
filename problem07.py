import math

#What is the 10,001st prime number?

def getprime(num):
	a = [x for x in xrange(1, 200000, 2) if is_prime(x)]
	return a[num-1]


def is_prime(a):
    b = [ i for i in xrange(2, int(math.sqrt(a)+1)) if (a%i == 0)]
    return True if len(b) == 0 else False

if __name__ == '__main__':
	print(getprime(10001))