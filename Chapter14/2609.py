def main():
	global num1, num2
	num1, num2 = getInput()

	gcd = getGCD()
	lcm = getLCM(gcd)

	print(gcd)
	print(lcm)
	

def getInput():
	num1, num2 = input().split()
	num1 = int(num1)
	num2 = int(num2)

	return num1, num2


def getGCD():
	return GCD(num1, num2)


def GCD(a, b):
	if((a % b) == 0):
		return b

	return GCD(b, a % b)

	
def getLCM(gcd):
	lcm = (num1 * num2) / gcd
	lcm = int(lcm)

	return lcm

main()