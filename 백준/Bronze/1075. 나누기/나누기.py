import sys
input = sys.stdin.readline

a = int(input())
b = int(input())

a = (a // 100) * 100

for i in range(100):
    if (a + i) % b == 0:
        print(f"{i:02d}")
        break
