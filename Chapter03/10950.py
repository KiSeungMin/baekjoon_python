def logic():
    countTestCase = int(input())
    
    for i in range(0, countTestCase):
        num1, num2 = getInput()
        print(num1 + num2)
    
    
def getInput():
    num1, num2 = map(int, input().split())
    return num1, num2
    
    
logic()
