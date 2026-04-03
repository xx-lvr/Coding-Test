import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
matrix = [list(input().strip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(x, y, visited):
    q = deque([(x, y)])
    visited[x][y] = True
    color = matrix[x][y]

    while q:
        ax, ay = q.popleft()
        for bx, by in dirs:
            nx, ny = ax + bx, ay + by
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and matrix[nx][ny] == color:
                visited[nx][ny] = True
                q.append((nx, ny))
    
def count_regions(visited):
    count = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j, visited)
                count += 1
    return count

normal_count = count_regions(visited)
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'G':
            matrix[i][j] = 'R'

visited = [[False] * n for _ in range(n)]
color_blind_count = count_regions(visited)
print(normal_count, color_blind_count)