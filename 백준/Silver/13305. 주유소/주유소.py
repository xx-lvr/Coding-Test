import sys
input = sys.stdin.readline

n = int(input())

first = list(map(int, input().split()))
second = list(map(int, input().split()))

result = 0
second_min = second[0]
for i in range(n - 1):
    result += second_min * first[i]
    if second[i + 1] < second_min:
        second_min = second[i + 1]

print(result)