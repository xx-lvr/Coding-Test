import sys
input = sys.stdin.readline

n = int(input())
d = 1

for _ in range(n):
    a, b = map(int, input().split())
    if d == a:
        d = b
    elif d == b:
        d = a

print(d)