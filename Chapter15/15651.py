def main():
	global LIMIT, LENGTH
	LIMIT, LENGTH = getInput()

	result_list = []
	getAnswer(result_list)


def getInput():
	LIMIT, LENGTH = input().split()
	LIMIT = int(LIMIT)
	LENGTH = int(LENGTH)

	return LIMIT, LENGTH


def getAnswer(result_list):

	for number in range(1, LIMIT + 1):
		result_list_copy = list(result_list)
		result_list_copy.append(number)

		if(len(result_list_copy) == LENGTH):
			printList(result_list_copy)

		else:
			getAnswer(result_list_copy)


def printList(list):
	for element in list:
		print(element, end=' ')

	print()


main()