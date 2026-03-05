import sys
input = sys.stdin.readline

a, b = map(int, input().split())
li = list(map(int, input().split()))
result = 0

for i in range(a):
    for j in range(i+1, a):
        for k in range(j+1, a):
            total = li[i] + li[j] + li[k]
            if total <= b:
                result = max(result, total)

print(result)