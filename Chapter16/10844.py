def main():
    global LENGTH
    LENGTH = int(input())
    
    global DP
    DP = getDPList(LENGTH)
    
    setDP()    
    
    ANSWER = getAnswer(1) % 1000000000
    
    #print(DP)
    
    print(ANSWER)
    
    
def getDPList(length):
    result_list = [[0 for i in range(0, length + 1)] for i in range(0, 10)]
    return result_list


def setDP():
    for i in range(1, 10):
        DP[i][1] = 1
        
    
def getAnswer(round):
    if(round == LENGTH):
        answer = getRoundSum(round)
        return answer
    
    else:
        for i in range(1, 9):
            DP[i + 1][round + 1] += DP[i][round]
            DP[i - 1][round + 1] += DP[i][round]
            
        DP[1][round + 1] += DP[0][round]
        DP[8][round + 1] += DP[9][round]
        
    return getAnswer(round + 1)
        

def getRoundSum(round):
    result = 0
    
    for i in range(0, 10):
        result += DP[i][round]
        
    return result

    
main()