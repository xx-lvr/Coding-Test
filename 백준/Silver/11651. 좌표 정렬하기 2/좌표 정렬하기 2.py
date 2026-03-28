n = int(input())
arr = []

for _ in range(n):
    first, second = input().split()
    arr.append((int(first), int(second)))

arr.sort(key=lambda x: (x[1], x[0]))

for first, second in arr:
    print(first, second)