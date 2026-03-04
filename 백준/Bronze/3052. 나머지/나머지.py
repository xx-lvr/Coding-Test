import sys
input = sys.stdin.readline

re = []
for _ in range(10):
    n = int(input())
    r = n % 42
    if r not in re:
        re.append(r)

print(len(re))