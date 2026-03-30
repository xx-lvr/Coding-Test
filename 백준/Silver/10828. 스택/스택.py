import sys
input = sys.stdin.readline

n = int(input())
stack = []

def push(x):
    stack.append(x)

def pop():
    if stack:
        return stack.pop()
    else:
        return -1

def size():
    return len(stack)

def empty():
    return 1 if not stack else 0

def top():
    if stack:
        return stack[-1]
    else:
        return -1

for _ in range(n):
    word = input().split()
    if word[0] == 'push':
        push(word[1])
    elif word[0] == 'pop':
        print(pop())
    elif word[0] == 'size':
        print(size())
    elif word[0] == 'empty':
        print(empty())
    elif word[0] == 'top':
        print(top())