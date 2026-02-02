def solution(my_string):
    answer = ''
    ans = 'aeiou'
    for i in my_string:
        if i not in ans:
            answer += i
    return answer