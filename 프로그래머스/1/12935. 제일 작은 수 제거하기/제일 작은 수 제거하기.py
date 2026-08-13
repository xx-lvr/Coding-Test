def solution(arr):
    low = min(arr)
    arr.remove(low)

    if len(arr) == 0:
        return [-1]
    else:
        return arr