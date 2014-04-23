#sum all the digits below 1000 that are divisible by 3 or 5

print(sum([x for x in range(1, 1000) if x%3 == 0 or x%5 == 0]))

#or

counter = 0
for x in range(0,1000):
	if x%3 ==0 or x%5 == 0:
		counter += x
print counter


