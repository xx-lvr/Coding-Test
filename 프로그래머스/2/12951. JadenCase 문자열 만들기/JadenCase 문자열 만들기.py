def solution(s):
    answer = ""
    first = True

    for i in s:
        if i == " ":
            answer += i
            first = True
        elif first:
            answer += i.upper()
            first = False
        else:
            answer += i.lower()

    return answer