import sys
input = sys.stdin.readline
case1list = []
case2list = []
m, n = map(int, input().split())
board = list(list(input().strip()) for _ in range(m))
ans = float('inf')
for i in range(m - 7):
    for j in range(n - 7):
        cnt = 0
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0:
                    if board[a][b] != 'W':
                        cnt += 1
                else:
                    if board[a][b] != 'B':
                        cnt += 1

        ans = min(ans, cnt, 64 - cnt)

print(ans)