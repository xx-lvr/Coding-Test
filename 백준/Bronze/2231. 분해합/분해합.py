n = int(input())
arr = list(range(1, n+1))

answer = 0
for i in arr:
    if i + sum(map(int, str(i))) == n:
        answer = i
        break

print(answer)