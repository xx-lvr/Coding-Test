import sys
input = sys.stdin.readline

n = int(input())
li = sorted(list(map(int, input().split())))


time = 0
total = 0
for i in li:
    time += i
    total += time

print(total)

## for i in range(1, n)
##     time[i] += time[i - 1]
## print(sum(time))