def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i == 0:
            answer.append(arr[i])
        elif arr[i] != arr[i-1]:
            answer.append(arr[i])
    return answer

## a = []
## for i in arr:
##     if not a or a[-1] != i:
##         a.append(i)
## return a