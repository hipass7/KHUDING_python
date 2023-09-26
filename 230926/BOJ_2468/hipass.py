# 안전영역
from collections import deque

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

result = 0
cnt = -1

while True:
    if cnt == 100:
        break
    cnt += 1
    res = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] <= cnt or visited[i][j] == True:
                continue
            queue = deque([])
            queue.append((i, j))
            while queue:
                x, y = queue.popleft()
                for t in range(4):
                    nx = x + dx[t]
                    ny = y + dy[t]

                    if nx < 0 or nx > (n-1) or ny < 0 or ny > (n-1) or visited[nx][ny] == True:
                        continue

                    if graph[nx][ny] <= cnt:
                        graph[nx][ny] = 0
                        continue

                    if graph[nx][ny] > cnt:
                        queue.append((nx, ny))
                        visited[nx][ny] = True
            res += 1
    if res < result:
        continue
    else:
        result = res

print(result)

