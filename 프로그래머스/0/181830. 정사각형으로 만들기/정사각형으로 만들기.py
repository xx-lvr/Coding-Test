def solution(arr):
    answer = []
    r_count = len(arr)
    c_count = len(arr[0])
    
    if r_count > c_count:
        for row in arr:
            answer.append(row + [0] * (r_count - c_count))
            
    elif c_count > r_count:
        for row in arr:
            answer.append(row)
            
        for _ in range(c_count - r_count):
            answer.append([0] * c_count)
            
    else:
        return arr
    
    return answer