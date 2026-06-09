def solution(array, commands):
    answer = []
    for command in commands:
        new_array = array[command[0] - 1 : command[1]]
        new_array.sort()
        k_num = new_array[command[2] - 1]
        answer.append(k_num)
    return answer