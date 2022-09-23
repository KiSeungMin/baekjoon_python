def main():
    global LENGTH, input_list
    LENGTH, input_list = getInput()

    global DP
    DP = []
    
    ANSWER = getAnswer()
    
    print(ANSWER)
    
    #print(DP)
    
    
def getInput():
    input_number = int(input())
    input_list = list(map(int, input().split()))
    
    return input_number, input_list


def getAnswer():
    DP.append(input_list[0])
    
    for element in input_list:
        if(element > DP[len(DP) - 1]):
            DP.append(element)
            
        else:
            for index in reversed(range(1, len(DP))):
                if(DP[index - 1] < element < DP[index]):
                    DP[index] = element
                    
            if(element < DP[0]):
                DP[0] = element
            
    
    return len(DP)

        
main()