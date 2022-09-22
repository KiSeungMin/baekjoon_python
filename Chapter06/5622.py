alphabetTable = [3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,8,9,9,9,10,10,10,10]

def main():
	input_str = input()

	print(getAnswer(input_str))

def getAnswer(str):

	answer = 0
	
	for element in str:
		asciiNumber = getAsciiNumber(element)
		answer = answer + alphabetTable[asciiNumber]

	return answer
		

def getAsciiNumber(char):
	return ord(char) - 65

main()