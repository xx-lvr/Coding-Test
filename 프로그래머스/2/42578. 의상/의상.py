def solution(clothes):
    clothes.sort(key=lambda x: x[1])
    
    answer = 1
    count = 1
    
    for i in range(len(clothes) - 1):
        if clothes[i][1] == clothes[i+1][1]:
            count += 1
        else:
            answer *= (count + 1)
            count = 1
            
    answer *= (count + 1)
    
    return answer - 1