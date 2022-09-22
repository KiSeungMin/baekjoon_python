def logic():
    
    list_size, input_list = getInput()
    
    getAndPrintAnswer(input_list)


def getInput():
    list_size = int(input())
    
    input_list = list(map(int, input().split(' ')))
    
    return list_size, input_list
    
    
def getAndPrintAnswer(input_list):
    
    input_list.sort()
        
    print(f'{input_list[0]} {input_list[len(input_list)-1]}')
    

logic()