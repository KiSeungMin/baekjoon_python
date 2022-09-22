def logic():
    list_size, input_list = getInput()

    max_element = getMaxElement(input_list)

    answer = getAnswer(input_list, max_element)

    print(answer)


def getInput():
    list_size = int(input())
    input_list = list(map(int, input().split()))

    return list_size, input_list


def getMaxElement(input_list):
    max_element = max(input_list)

    return max_element


def getAnswer(input_list, max_element):

    answer = 0

    for element in input_list:
        element = (element / max_element) * 100
        answer += element

    list_size = len(input_list)

    answer = answer / list_size

    return answer


logic()
