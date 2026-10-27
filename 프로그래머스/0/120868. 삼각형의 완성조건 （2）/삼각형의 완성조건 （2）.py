def solution(sides):
    a = sides[0]
    b = sides[1]
    count = 0

    for x in range(1, a + b):
        if abs(a - b) < x:
            count += 1

    return count