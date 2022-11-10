def main():
    global gap, input_list
    amount, gap = map(int, input().split())
    
    input_list = list(map(int, input().split()))
    
    answer = getAnswer()
    
    print(answer)
    
    
def getAnswer():
    sum = getSum(0, gap)
    answer = sum
    
    start = 0
    end = start + gap
    
    while(end < len(input_list)):
        diff = input_list[end] - input_list[start]
        sum += diff
        
        if(sum > answer):
            answer = sum
            
        start, end = start + 1, end + 1
        
    return answer


def getSum(start, end):
    sum = 0
    for i in range(start, end):
        sum += input_list[i]
        
    return sum
        
        
main()