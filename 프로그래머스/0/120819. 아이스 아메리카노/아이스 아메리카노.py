def solution(money):
    p = 5500
    c = money // p
    ch = money % p
    
    return [c, ch]
