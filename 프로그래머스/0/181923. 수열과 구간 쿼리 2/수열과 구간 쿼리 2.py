def solution(arr, queries):
    answer = []

    for s, e, k in queries:
        min_v = 1000001

        for i in range(s, e + 1):
            if arr[i] > k:
                if arr[i] < min_v:
                    min_v = arr[i]

        if min_v == 1000001:
            answer.append(-1)
        else:
            answer.append(min_v)

    return answer