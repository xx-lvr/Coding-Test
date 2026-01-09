import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    l = pow(a, b, 10)
    print(10 if l == 0 else l)