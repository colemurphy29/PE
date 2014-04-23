
#0.1 seconds

totalsum = 1
currentNumber = 1
currentIndex = 2
currentLine = 0
while currentLine<500:
	for x in range (0,4):
		totalsum += (currentNumber + currentIndex)
		currentNumber += currentIndex
	currentIndex +=2
	currentLine += 1

print totalsum

#answer = 669171001