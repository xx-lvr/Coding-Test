import sys
input = sys.stdin.readline
n = int(input())
arr = []

for _ in range(n):
    n, m = map(int, input().split())
    arr.append((n, m))
arr.sort(key=lambda x: (x[0], x[1]))

for n, m in arr:
    print(n, m)