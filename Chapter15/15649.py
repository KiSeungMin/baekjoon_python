def main():
	global LIMIT, LENGTH
	LIMIT, LENGTH = getInput()

	result_list = []
	is_number_exist = list(False for i in range(LIMIT + 1))

	getAnswer(result_list, is_number_exist)
	

def getInput():
	LIMIT, LENGTH = input().split()
	LIMIT = int(LIMIT)
	LENGTH = int(LENGTH)

	return LIMIT, LENGTH


def getAnswer(result_list, is_number_exist):	

	for number in range(1, LIMIT + 1):
		if(not is_number_exist[number]):
			result_list_copy = list(result_list)
			result_list_copy.append(number)
			is_number_exist_copy = list(is_number_exist)
			is_number_exist_copy[number] = True

			if(len(result_list_copy) == LENGTH):
				printList(result_list_copy)

			else:
				getAnswer(result_list_copy, is_number_exist_copy)


def printList(list):
	for element in list:
		print(element, end = ' ')

	print()

	
main()