def factorial(n):
    answer = 1
    for i in range(1, n + 1):
        answer *= i
    return answer


def solution(balls, share):
    answer = factorial(balls) // (factorial(share) * factorial(balls - share))
    return answer