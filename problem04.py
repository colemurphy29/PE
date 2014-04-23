
#Find the largest palindrome made from the product of two 3-digit numbers.

# def p():
# 	palindrome = set()
# 	for x in xrange(100,1000):
# 		for y in xrange(100,1000):
# 			b = x*y
# 			if str(b) == str(b)[::-1]:
# 				palindrome.add(b)
# 	return max(palindrome)

#or

print max(set([x*y for x in xrange(100,1000) for y in xrange(100,1000) if str(x*y) == str(x*y)[::-1]]))

