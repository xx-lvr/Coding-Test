import sys
input = sys.stdin.readline

n = int(input())
c = 0
d = 5
while n / d > 0 :
    c += n // d
    d *= 5

print(c)