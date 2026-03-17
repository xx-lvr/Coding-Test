import sys
input = sys.stdin.readline

n = int(input())
wo = []

for _ in range(n):
    word = input().strip()
    if word not in wo:
        wo.append(word)

wo.sort()
wo.sort(key=len)

for w in wo:
    print(w)