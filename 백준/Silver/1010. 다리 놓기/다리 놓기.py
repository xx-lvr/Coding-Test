import math

def com(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(com(M, N))