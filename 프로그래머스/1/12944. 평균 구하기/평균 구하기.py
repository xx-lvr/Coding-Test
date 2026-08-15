def solution(arr):
    answer = 0
    for i in arr:
        answer += i
    a = answer / len(arr)
    return a