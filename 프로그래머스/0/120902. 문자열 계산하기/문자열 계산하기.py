def solution(my_string):
    answer = my_string.split()
    result = int(answer[0])
    
    for i in range(1, len(answer), 2):
        op = answer[i]
        num = int(answer[i+1])
        if op == '+':
            result += num
        elif op == '-':
            result -= num
    return result
