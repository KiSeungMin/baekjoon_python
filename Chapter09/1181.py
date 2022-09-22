def main():
	input_string_arr = getInput()

	sorted_arr = sortInputStrings(input_string_arr)

	printAnswer(sorted_arr)

def getInput():
	INPUT_SIZE = int(input())
	input_string_arr = list()

	for i in range(INPUT_SIZE):
		input_str =  input()
		input_string_arr.append(input_str)


	input_string_arr = list(set(input_string_arr))
	
	return input_string_arr


def sortInputStrings(string_arr):
	string_arr.sort()
	string_arr.sort(key = lambda x : len(x))
	return string_arr


def printAnswer(arr):
	for element in arr:
		print(element)


main()