def solution(i, j, k):
    answer = 0
    ans = str(k)
    for num in range(i, j+1):
        answer += str(num).count(ans)
    return answer