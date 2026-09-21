def solution(arr):
    cnt = 0
    while True:
        answer = []
        for i in arr:
            if i >= 50 and i % 2 == 0:
                answer.append(i // 2)
            elif i < 50 and i % 2 == 1:
                answer.append(i * 2 + 1)
            else:
                answer.append(i)
        if arr == answer:
            break
        arr = answer
        cnt += 1
    return cnt