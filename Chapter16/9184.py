INF = 99999999999
LIMIT = 21

def main():
    global logic_table
    logic_table = makeLogicTable()

    input_list = getInput()

    while(not isInputEnd(input_list)):
        answer = getAnswer(input_list[0], input_list[1], input_list[2])

        print(f'w({input_list[0]}, {input_list[1]}, {input_list[2]}) = {answer}')

        input_list = getInput()


def makeLogicTable():
    return [[[INF for col in range(LIMIT)] for row in range(LIMIT)] for depth in range(LIMIT)]


def getInput():
    input_list = list(map(int, input().split()))
    return input_list


def isInputEnd(input_list):
    for element in input_list:
        if(element != -1):
            return False

    return True


def getAnswer(num1, num2, num3):
    if(num1 == 0 or num2 == 0 or num3 == 0):
        if(0 <= num1 < LIMIT and 0 <= num2 < LIMIT and 0 <= num3 < LIMIT):
            logic_table[num1][num2][num3] = 1
        return 1

    if(num1 < 0 or num2 < 0 or num3 < 0):
        return 1

    if(num1 > 20 or num2 > 20 or num3 > 20):
        return getAnswer(20, 20, 20)

    if(logic_table[num1][num2][num3] != INF):
        result = logic_table[num1][num2][num3]

    elif(num1 < num2 < num3):
        result = getAnswer(num1, num2, num3 - 1) + getAnswer(num1, num2 - 1, num3 - 1) - getAnswer(num1, num2 - 1, num3)

    else:
        result = getAnswer(num1 - 1, num2, num3) + getAnswer(num1 - 1, num2 - 1, num3) + getAnswer(num1 - 1, num2, num3 - 1) - getAnswer(num1 - 1, num2 - 1, num3 - 1)

    logic_table[num1][num2][num3] = result
    return result


main()

