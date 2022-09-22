LIMIT = 26
alphabetIndexArr = list(-1 for i in range(0, LIMIT))

def main():
	input_str = input()

	logic(input_str)

	printAnswer()

def logic(str):
	for index in range(len(str)):
		asciiNumber = getAsciiNumber(str[index])

		if(alphabetIndexArr[asciiNumber] == -1):
			alphabetIndexArr[asciiNumber] = index

def getAsciiNumber(char):
	return ord(char) - 97

def printAnswer():
	for element in alphabetIndexArr:
		print(element, end=' ')


main()