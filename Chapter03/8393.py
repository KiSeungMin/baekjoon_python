def logic():
    endNumber = int(input())
    
    print(getSum(endNumber))
    
def getSum(endNumber):
    return ((endNumber)*(endNumber + 1))//2
    
logic()

