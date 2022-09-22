LIMIT = 10001

def logic():
	isSelfNumber = list(True for i in range(0, LIMIT))

	getSelfNumber(isSelfNumber)

	printSelfNumber(isSelfNumber)


def getSelfNumber(isSelfNumber):
	for i in range(1, LIMIT):
		mySelfNumber = makeSelfNumber(i)

		if(mySelfNumber < LIMIT):
			isSelfNumber[mySelfNumber] = False

def makeSelfNumber(number):
	selfNumber = number
	numberStr = str(number)

	for element in numberStr:
		selfNumber += int(element)

	return selfNumber

def printSelfNumber(isSelfNumber):
	for i  in range(1, LIMIT):
		if(isSelfNumber[i]):
			print(i)

logic()
	