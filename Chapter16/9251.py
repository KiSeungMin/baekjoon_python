def main():
    global str1, str2
    str1, str2 = getInput()
    
    global DP
    DP = getDPList()
    
    ANSWER = getAnswer()
    
    #print(DP)
    print(ANSWER)


def getInput():
    str1 = input()
    str2 = input()
    
    return str1, str2


def getDPList():
    row = len(str1)
    col = len(str2)
    
    result = [[0 for x in range(0, col)] for y in range(0, row + 1)]
    return result


def getAnswer():
    for str1_index in range(0, len(str1)):
        for str2_index in range(0, len(str2)):
            
            if (str2_index == 0):
                DP[str1_index + 1][str2_index] = DP[str1_index][str2_index]
                
                if(str1[str1_index] == str2[str2_index]):
                    DP[str1_index + 1][str2_index] = 1
            
            else:
                if(str1[str1_index] == str2[str2_index]):
                    DP[str1_index + 1][str2_index] = DP[str1_index][str2_index - 1] + 1
                else:
                    DP[str1_index + 1][str2_index] = getMax(DP[str1_index][str2_index], DP[str1_index + 1][str2_index - 1])
                
                
    return DP[len(str1)][len(str2) - 1]
            

def getMax(num1, num2):
    if(num1 > num2):
        return num1
    
    return num2


main()