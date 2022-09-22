def main():
	global LIMIT, LENGTH
	LIMIT , LENGTH = getInput()

	result_list = []
	getAnswer(result_list, 1)


def getInput():
	LIMIT, LENGTH = input().split()
	LIMIT = int(LIMIT)
	LENGTH = int(LENGTH)

	return LIMIT, LENGTH


def getAnswer(result_list, startNumber):
	for number in range(startNumber, LIMIT + 1):
		
		result_list_copy = list(result_list)
		result_list_copy.append(number)

		if(len(result_list_copy) == LENGTH):
			printList(result_list_copy)

		else:
			getAnswer(result_list_copy, number + 1)


def printList(result_list):
	for element in result_list:
		print(element, end=' ')

	print()
		

main()