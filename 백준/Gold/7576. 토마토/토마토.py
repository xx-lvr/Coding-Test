import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
q = deque()

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            q.append((i, j))

while q:
    x, y = q.popleft()
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
            box[nx][ny] = box[x][y] + 1
            q.append((nx, ny))

ans = 0
for i in box:
    for j in i:
        if j == 0:
            print(-1)
            sys.exit(0)
        ans = max(ans, j)

print(ans - 1)