import sys
input = sys.stdin.readline
n = int(input())
queue = []

def push(x):
    queue.append(x)

def pop():
    if queue:
        return queue.pop(0)
    else:
        return -1

def size():
    return len(queue)

def empty():
    return 1 if not queue else 0

def front():
    if queue:
        return queue[0]
    else:
        return -1

def back():
    if queue:
        return queue[-1]
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
    elif word[0] == 'front':
        print(front())
    elif word[0] == 'back':
        print(back())