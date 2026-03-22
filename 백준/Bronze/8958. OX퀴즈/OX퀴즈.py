import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    put = input().strip()
    score = 0
    count = 0
    for i in put:
        if i == "O":
            count += 1
            score += count
        else:
            count = 0
    print(score)