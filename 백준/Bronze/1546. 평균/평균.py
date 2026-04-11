import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

max_arr = max(arr)
total = 0
for score in arr:
    total += score / max_arr * 100

print(total / n)