def logic():
    num1, num2 = getInput()
    getAnswer(num1, num2)
    
def getInput():
    num1, num2 = map(int, input().split())
    return num1, num2
    
def getAnswer(num1, num2):
    if(num1 > num2):
        print(">")
    elif(num1 < num2):
        print("<")
    else:
        print("==")
        
        
logic()
    