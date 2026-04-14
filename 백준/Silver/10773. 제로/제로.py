import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    s = int(input())
    if s == 0:
        stack.pop()
    else:
        stack.append(s)

print(sum(stack))