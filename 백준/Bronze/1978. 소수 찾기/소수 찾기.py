import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

result = 0

for i in nums:
    if i > 1:
        count = 0
        for j in range(2, i):
            if i % j == 0:
                count += 1
        
        if count == 0:
            result += 1

print(result)