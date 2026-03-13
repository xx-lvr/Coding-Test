import sys
input = sys.stdin.readline

n = int(input())

first = list(map(int, input().split()))
second = list(map(int, input().split()))

result = 0

for i in range(n - 1):
    result += second[0] * first[i]
    if second[i + 1] < second[0]:
        second[0] = second[i + 1]

print(result)