def solution(a, b):
    min_val = min(a, b)
    max_val = max(a, b)
    total = 0
    for i in range(min_val, max_val + 1):
        total += i
    return total