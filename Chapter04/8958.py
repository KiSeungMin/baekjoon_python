#import sys

def logic():
	caseAmount = int(input())

	for case in range(0, caseAmount):
		caseInputString = input()

		answer = getAnswer(caseInputString)

		print(answer)

def getAnswer(caseInputString):
	answer = 0
	scoreNow = 0
	
	for element in caseInputString:
		if(element == 'O'):
			scoreNow += 1

		elif(element =='X'):
			scoreNow = 0

		answer += scoreNow

	return answer

logic()