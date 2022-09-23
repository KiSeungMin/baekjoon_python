def main():
    global LENGTH, input_lists
    LENGTH, input_lists = getInput()

    global DP
    DP = []
    
    ANSWER = getAnswer()
    
    print(ANSWER)
    #print(DP)
    
    
def getInput():
    LENGTH = int(input())
    input_lists = []
    
    for i in range(0, LENGTH):
        input_list = list(map(int, input().split()))
        input_lists.append(input_list)
        
    input_lists.sort()
        
    return LENGTH, input_lists


def getAnswer():
    DP.append(input_lists[0][1])
    
    for element in input_lists:
        number = element[1]
        
        if(number > DP[len(DP) - 1]):
            DP.append(number)
            
        else:
            for index in reversed(range(1, len(DP))):
                if(DP[index - 1] < number < DP[index]):
                    DP[index] = number
                    
            if(number < DP[0]):
                DP[0] = number
                

    return LENGTH - len(DP)
    
    
main()
    
    


