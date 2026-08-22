def solution(myString, pat):
    answer = ''
    for i in range(len(myString)):
        answer += myString[i]
        if answer.endswith(pat):
            last = answer
    return last