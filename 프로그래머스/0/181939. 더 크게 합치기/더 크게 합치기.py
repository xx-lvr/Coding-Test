def solution(a, b):
    m = str(a) + str(b)
    n = str(b) + str(a)
    
    return max(int(m), int(n))