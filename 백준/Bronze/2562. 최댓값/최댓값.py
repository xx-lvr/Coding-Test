import sys
input = sys.stdin.readline

answer = 0
ans = 0

for i in range(9):
    num = int(input())
    if num > answer:
        answer = num
        ans = i + 1

print(answer)
print(ans)