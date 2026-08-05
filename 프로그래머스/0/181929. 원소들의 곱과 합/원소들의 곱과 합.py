def solution(num_list):
    answer = 1
    ans = 0
    for i in num_list:
        answer *= i
        ans += i
        
    if answer < ans ** 2:
        return 1
    else:
        return 0