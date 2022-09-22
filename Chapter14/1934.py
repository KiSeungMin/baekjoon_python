def main():
	caseAmount = int(input())
	
	for i in range(caseAmount):
		num1, num2 = getInput()
		logic(num1, num2)


def getInput():
	num1, num2 = input().split()
	num1 = int(num1)
	num2 = int(num2)

	return num1, num2
	

def logic(num1, num2):
	lcm = getLCM(num1, num2)
	print(lcm)


def getLCM(num1, num2):
	gcd = GCD(num1, num2)
	lcm = (num1 * num2) / gcd
	lcm = int(lcm)

	return lcm
	

def GCD(a, b):
	if((a % b) == 0):
		return b

	return GCD(b, a % b)


main()