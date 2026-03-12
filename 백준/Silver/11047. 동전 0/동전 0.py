import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = sorted([int(input()) for _ in range(n)], reverse=True)

result = 0
for coin in coins:
    result += k // coin
    k %= coin
    if k == 0:
        break
print(result)