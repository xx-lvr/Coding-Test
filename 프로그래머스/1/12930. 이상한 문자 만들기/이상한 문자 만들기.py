def solution(s):
    answer = ''
    word = 0
    for i in range(len(s)):
        if s[i] == ' ':
            answer += s[i]
            word = 0
        else:
            if word % 2 == 0:
                answer += s[i].upper()
            else:
                answer += s[i].lower()
            word += 1
    
    return answer