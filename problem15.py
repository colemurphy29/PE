from math import factorial

def findnum(row, pos):
	#n choose k
	return (factorial(row)/(factorial(pos) * factorial(row - pos)))


if __name__ == '__main__':
	print(findnum(40, 20))