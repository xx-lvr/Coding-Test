def solution(s):
    answer = 0
    last = 0
    s = s.split()
    for i in s:
        if i != 'Z':
            answer += int(i)
            last = int(i)
        else:
            answer = answer - last
    return answer