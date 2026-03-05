import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())
d = int(input())

result = a + b + c + d + 300

if result <= 1800:
    print("Yes")
else:
    print("No")