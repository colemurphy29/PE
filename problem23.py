import math

#not terribly fast - 10.5 seconds 

def divisorGenerator(n):
    large_divisors = []
    for i in xrange(1, int(math.sqrt(n) + 1)):
        if n % i is 0:
            yield i
            if i is not n / i:
                large_divisors.insert(0, n / i)
    for divisor in large_divisors:
        yield divisor

abundant = set()
#check if a number is abundant
for x in range(1, 20200):
	divisorlist = list(divisorGenerator(x))
	total = 0
	for y in range(0, len(divisorlist)-1):
		total += divisorlist[y]
	if total > x:
		abundant.add(x)


abundantsum = set([(e+f) for e in abundant for f in abundant])
nonabundantsum = []
for num3 in range(1, 20200):
	if num3 not in abundantsum:
		nonabundantsum.append(num3)
print (sum(nonabundantsum))