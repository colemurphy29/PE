
#0.9 seconds

import math
a = 0
z = 0
for x in range (1,100):
	for y in range(1,100):
		a = pow(x,y)
		astr = str(a)
		b = 0
		for f in range(0, len(astr)):
			q = int(astr[f])
			b = b+q
		if b > z:
			z = b
print str(z)