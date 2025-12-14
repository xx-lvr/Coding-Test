import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    num = input().strip()
    sq = str(int(num) ** 2)

    if sq.endswith(num):
        print("YES")
    else:
        print("NO")