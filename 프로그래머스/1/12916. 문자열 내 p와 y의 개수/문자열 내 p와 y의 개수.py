def solution(s):
    result = 0
    yresult = 0
    s = s.lower()
    for i in s:
        if i == 'p':
            result += 1
        elif i == 'y':
            yresult += 1
    
    if result == yresult:
        return True
    else:
        return False