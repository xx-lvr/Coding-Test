import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

answer = -1

for x in range(0, n + 1):
    a = 0
    for v in arr:
        if v == x:
            a += 1
    if a == x:
        answer = x

print(answer)