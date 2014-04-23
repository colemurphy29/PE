
#1.6 seconds - find the first fibonacci number with 1000 digits


def fiblength(n):
	a, b = 0, 1
	count = 2
	while len(str(b)) < n+1:
		a, b = b, a+b 
		if len(str(b)) == n:
			print(count)
			break
		count += 1

if __name__ == '__main__':
	fiblength(1000)