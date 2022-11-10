def main():
    size, cycle = input().split()
    cycle = int(cycle)
    input_list = list(map(int, input().split()))
    
    global sum_arr
    sum_arr = makeSumArray(input_list)
    
    for i in range(0, cycle):
        start, end = map(int, input().split())
        print(getSum(start, end))    
        
def makeSumArray(input_list):
    
    result_list = [0, input_list[0]]
    
    for i in range(1, len(input_list)):
        input_list[i] = input_list[i] + input_list[i-1]
        result_list.append(input_list[i])
        
    return result_list

    
def getSum(start, end):
    answer = sum_arr[end] - sum_arr[start - 1];
    return answer


main()