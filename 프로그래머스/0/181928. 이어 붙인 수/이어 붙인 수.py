def solution(num_list):
    answer = ""
    ans = ""
    for i in range(len(num_list)):
        if num_list[i] % 2 == 1:
            answer += str(num_list[i])
        else:
            ans += str(num_list[i])
    return int(answer) + int(ans)