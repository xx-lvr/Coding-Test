def solution(strArr):
    answer = []
    for a, b in enumerate(strArr):
        if a % 2 == 0:
            answer.append(b.lower())
        else:
            answer.append(b.upper())
    return answer