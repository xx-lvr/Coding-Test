def solution(myString, pat):
    answer = ''
    count = 0
    for i in range(len(myString)):
        answer = myString[i:i+len(pat)]
        if answer == pat:
            count += 1
    return count