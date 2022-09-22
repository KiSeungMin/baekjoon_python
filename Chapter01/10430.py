from sys import stdin

def init():
    num1, num2, num3 = map(int, stdin.readline().split())
    print_answer(num1, num2, num3)
    
def print_answer(num1, num2, num3):
    print((num1 + num2) % num3)
    print(((num1 % num3) + (num2 % num3)) % num3)
    print((num1 * num2) % num3)
    print(((num1 % num3) * (num2 % num3)) % num3)
    
init()