def solution(arr):
    l = len(arr)
    answer = 1
    while answer < l:
        answer *= 2
    while len(arr) < answer:
        arr.append(0)
    
    return arr