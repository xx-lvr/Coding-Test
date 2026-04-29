def solution(numLog):
    result = []
    for i in range(1, len(numLog)):
        a = numLog[i] - numLog[i-1]
        if a == 1:
            result.append("w")
        elif a == -1:
            result.append("s")
        elif a == 10:
            result.append("d")
        elif a == -10:
            result.append("a")
    return "".join(result)
