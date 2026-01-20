def solution(num_list):
    answer = 0
    ans = 0
    
    for i in range(len(num_list)):
        if i % 2 == 0:
            answer += num_list[i]
        else:
            ans += num_list[i]
    
    return max(answer, ans)