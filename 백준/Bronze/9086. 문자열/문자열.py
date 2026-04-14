import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    a = input().strip()
    print(a[0] + a[-1])