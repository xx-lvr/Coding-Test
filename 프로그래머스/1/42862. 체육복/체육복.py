def solution(n, lost, reserve):
    lost = set(lost)
    reserve = set(reserve)

    both = lost & reserve
    lost -= both
    reserve -= both

    for i in sorted(reserve):
        if i - 1 in lost:
            lost.remove(i - 1)
        elif i + 1 in lost:
            lost.remove(i + 1)

    return n - len(lost)