def solution(strArr):
    answer = 0
    count = {}

    for i in strArr:
        length = len(i)

        if length in count:
            count[length] = count[length] + 1
        else:
            count[length] = 1

    for i in count:
        if count[i] > answer:
            answer = count[i]

    return answer