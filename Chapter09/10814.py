def main():
	input_list = getInput()

	sorted_list = sortInputList(input_list)

	printAnswer(sorted_list)

def getInput():
	input_size = int(input())
	input_list = list()
	order = 0

	for i in range(input_size):
		age, name = input().split()
		age = int(age)
		list_now = [age, name, order]

		input_list.append(list_now)

		order = order +  1

	return input_list

def sortInputList(input_list):

	input_list.sort(key = lambda x : (x[0], x[2]))
	return input_list

def printAnswer(sorted_list):
	for element in sorted_list:
		print(element[0], element[1])

main()