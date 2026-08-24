def solution(food):
    answer = ''
    count = 0
    for i in range(1, len(food)):
        count = food[i] // 2
        answer += str(i) * count
    return answer + "0" + answer[::-1]