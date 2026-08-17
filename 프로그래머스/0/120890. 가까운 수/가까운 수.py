def solution(array, n):
    min_v = 101
    min_i = 0
    
    for i in range(len(array)):
        k = abs(array[i] - n)
        
        if k < min_v:
            min_v = k
            min_i = i
        elif k == min_v and array[i] < array[min_i]:
            min_i = i
    
    return array[min_i]