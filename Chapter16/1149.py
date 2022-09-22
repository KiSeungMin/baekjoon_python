def main():
    global LIMIT, input_lists
    LIMIT, input_lists = getInput()
    
    ANSWER = logic(input_lists)
    
    print(ANSWER)
    
    
def getInput():
    LIMIT = int(input())
    input_lists = []
    
    for i in range(0, LIMIT):
        input_list = list(map(int, input().split()))
        input_lists.append(input_list)
    
    return LIMIT, input_lists


def logic(DP):
    for row in range(1, LIMIT):
        for col in range(0, 3):
            if(col == 0):
                DP[row][col] += getMinNum(DP[row-1][1], DP[row-1][2])
            elif(col == 1):
                DP[row][col] += getMinNum(DP[row-1][0], DP[row-1][2])
            elif(col == 2):
                DP[row][col] += getMinNum(DP[row-1][0], DP[row-1][1])
            
    return getAnswer(DP)


def getAnswer(DP):
    ANSWER = 99999999999
    
    for col in range(0, 3):
        ANSWER = getMinNum(ANSWER, DP[LIMIT - 1][col])
        
    return ANSWER
    
                
def getMinNum(num1, num2):
    if(num1 > num2):
        return num2
    
    return num1

main()