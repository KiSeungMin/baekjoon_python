def main():
    global DP, LIMIT
    LIMIT = getInput()
    
    DP = getDPList(LIMIT)
    
    ANSWER = getAnswer([1], 0)
    
    #printDPList()
    
    print(ANSWER)
    
    
def getInput():
    input_number = int(input())
    return input_number


def getDPList(size):
    dp_list = [-1 for i in range(0, size + 1)]
    return dp_list
    
    
def printDPList():
    for element in DP:
        print(element)
        
    
def getAnswer(number_list, round):
    
    next_number_list = []
    
    for element in number_list:
        if(element > LIMIT):
            continue
        
        elif(element == LIMIT):
            return round
        
        else:
            if(DP[element] == -1):
                DP[element] = round
                
                next_number_list.append(element * 3)
                next_number_list.append(element * 2)
                next_number_list.append(element + 1)
                
    return getAnswer(next_number_list, round + 1)


main()