def solution(intStrs, k, s, l):
    answer = []
    for i in range(len(intStrs)):
        value = int(intStrs[i][s:s+l])
        if value > k:
            answer.append(value)
    return answer