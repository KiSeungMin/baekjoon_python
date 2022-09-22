def main():
	global input_str, part_strings_set
	input_str = getInput()
	part_strings_set = set()

	getPartStrings()

	printAnswer()


def getInput():
	input_str = input()
	return input_str
	

def getPartStrings():
	for startIndex in range(0, len(input_str)):
		result_str = ""
		
		for index in range(startIndex, len(input_str)):
			result_str += input_str[index]
			part_strings_set.add(result_str)
		

def printAnswer():
	print(len(part_strings_set))


main()