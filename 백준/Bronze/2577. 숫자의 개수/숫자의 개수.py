import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())
abc = a * b * c
result = str(abc)
sorted_result = sorted(result)
for i in range(10):
    print(sorted_result.count(str(i)))