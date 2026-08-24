def solution(numbers, k):
    answer = 0
    for i in range(1, k):
        answer = (answer + 2) % len(numbers)
    return numbers[answer]