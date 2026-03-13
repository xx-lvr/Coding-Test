import sys
input = sys.stdin.readline

n = int(input().strip())
li = sorted(list(map(int, input().split())))


time = 0
total = 0
for i in li:
    time += i
    total += time

print(total)