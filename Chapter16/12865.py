from sys import stdin

def main():
    global AMOUNT, LIMIT, input_lists
    AMOUNT, LIMIT, input_lists = getInput()
    
    print(input_lists)
    
    
def getInput():
    [AMOUNT, LIMIT] = map(int, input().split())
    
    input_lists = [list(map(int, stdin.readline().split())) for i in range(0, AMOUNT)]
    
    return AMOUNT, LIMIT, input_lists


main()