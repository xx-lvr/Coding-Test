def solution(array, commands):
    answer = []
    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]
        new_array = array[i - 1 : j]
        new_array.sort()
        k_num = new_array[k - 1]
        answer.append(k_num)
    return answer