from sys import stdin

goal_list = [1, 1, 2, 2, 2, 8]

def init():
    input_list = list(map(int, stdin.readline().split()))
    
    answer_list = [0,0,0,0,0,0]    
    get_answer(input_list, answer_list)
    
    print_answer(answer_list)

def get_answer(input_list, answer_list):
    for i in range(0, 6):
        answer_list[i] = goal_list[i] - input_list[i]
        
def print_answer(answer_list):
    for element in answer_list:
        print(element, end=' ')
        
init()