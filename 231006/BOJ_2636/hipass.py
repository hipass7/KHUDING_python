# 치즈
from collections import deque

h, w = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(h)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

queue = deque([])


cnt = []
while True:
    some = False
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 0:
                queue.append((i, j))
                some = True
                break
        if some:
            break

    visited = [[0] * w for _ in range(h)]
    cnt1 = 0
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                continue
            if graph[x][y] == 0:
                if graph[nx][ny] == 1:
                    cnt1 += 1
                    graph[nx][ny] = -1
            else:
                break

            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))

    print(graph)
    for _1 in range(h):
        for _2 in range(w):
            if graph[_1][_2] == -1:
                graph[_1][_2] = 0

    cnt.append(cnt1)

    if cnt1 == 0:
        break

print(len(cnt) - 1)
print(cnt[len(cnt) - 2])