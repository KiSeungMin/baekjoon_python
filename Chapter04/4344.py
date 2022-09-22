import sys

def init():
	caseAmount = int(input())

	for i in range(0, caseAmount):
		logic()


def logic():
	input_list, list_size = getInput()

	getAverage(input_list)
	
	average = getAverage(input_list)
	
	answer = getAnswer(input_list, average)
		
	print('%.3f'%answer + '%')

def getInput():
	input_str = sys.stdin.readline().rstrip()
	
	input_list = list(map(int, input_str.split()))
	
	list_size = input_list.pop(0)

	return input_list, list_size


def getAverage(input_list):

	sum = 0

	for element in input_list:
		sum += element

	list_size = len(input_list)
	
	return sum / list_size

def getAnswer(input_list, average):

	countOverAverage = 0
	
	for element in input_list:
		if (element > average):
			countOverAverage += 1

	list_size = len(input_list)
	
	answer = round((countOverAverage / list_size) * 100, 3)

	return answer

init()