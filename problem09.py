import math

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.
#brute force  >> .1 seconds

def q09():
	for a in xrange(0,500):
		for b in xrange(0,a):
			c = a**2 - b**2
			d = math.sqrt(c)
			if d**2 == c and d<b:
				if(a+b+d)==1000:
					print(int(a*b*d))

if __name__ == '__main__':
	q09()
