import itertools

a = itertools.permutations([0,1,2,3,4,5,6,7,8,9])

for index, x in enumerate(a):
	if index == 1000000:
		print(''.join(str(i) for i in x))
		break