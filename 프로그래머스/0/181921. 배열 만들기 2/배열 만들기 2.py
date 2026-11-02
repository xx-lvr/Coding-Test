def solution(l, r):
    answer = []

    for i in range(l, r + 1):
        s = str(i).replace('0', '').replace('5', '')

        if not s:
            answer.append(i)

    return answer if answer else [-1]