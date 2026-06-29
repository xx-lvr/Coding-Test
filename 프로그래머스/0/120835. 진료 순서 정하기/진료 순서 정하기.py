def solution(emergency):
    answer = []
    for i in range(len(emergency)):
        answer.append(emergency[i])
    
    answer.sort(reverse=True)
    
    result = []
    for j in emergency:
        result.append(answer.index(j) + 1)
    return result
