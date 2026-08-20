def solution(numbers):
    total = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                total.append(numbers[i] + numbers[j])
    total = list(set(total))
    total.sort()
    return total