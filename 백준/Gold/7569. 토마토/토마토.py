import sys
from collections import deque

input = sys.stdin.readline
m, n, h = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
dirs = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

q = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:
                q.append((i, j, k))

while q:
    x, y, z = q.popleft()
    for dx, dy, dz in dirs:
        nx, ny, nz = x + dx, y + dy, z + dz
        if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and box[nx][ny][nz] == 0:
            box[nx][ny][nz] = box[x][y][z] + 1
            q.append((nx, ny, nz))

ans = 0
for i in box:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                sys.exit(0)
            ans = max(ans, k)
print(ans - 1)