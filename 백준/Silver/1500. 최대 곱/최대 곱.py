s, k = map(int, input().split())

base = s // k
re = s % k

result = 1

for i in range(k):
    if i < re:
        result *= (base + 1)
    else:
        result *= base

print(result)