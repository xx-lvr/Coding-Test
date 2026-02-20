import sys
input = sys.stdin.readline

a = int(input())
for _ in range(a):
    b = input().strip()
    count = 0
    v = True
    for i in b:
        if i == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            v = False
            break
    if count != 0:
        v = False
    print("YES" if v else "NO")