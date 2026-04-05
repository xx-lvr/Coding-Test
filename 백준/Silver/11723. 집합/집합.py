import sys
input = sys.stdin.readline
n = int(input())

def add(x):
    return x + 1

def remove(x):
    return x - 1

def check(x):
    return 1 if x in s else 0

def toggle(x):
    if x in s:
        s.remove(x)
    else:
        s.add(x)

def all():
    return set(range(1, 21))

def empty():
    return set()

s = set()
for _ in range(n):
    word = input().split()
    if word[0] == 'add':
        s.add(int(word[1]))
    elif word[0] == 'remove':
        s.discard(int(word[1]))
    elif word[0] == 'check':
        print(check(int(word[1])))
    elif word[0] == 'toggle':
        toggle(int(word[1]))
    elif word[0] == 'all':
        s = all()
    elif word[0] == 'empty':
        s = set()