def solution(a, b, c):
    n = a + b + c
    m = n * (a**2 + b**2 + c**2)
    o = m * (a**3 + b**3 + c**3)

    if a == b == c:
        return o
    elif a == b or b == c or a == c:
        return m
    else:
        return n