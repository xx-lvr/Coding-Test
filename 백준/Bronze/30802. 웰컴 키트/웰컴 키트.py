import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))
t, p = map(int, input().split())

ts = sum((size + t - 1) // t for size in s)

pb = n // p
ps = n % p

print(ts)
print(pb, ps)