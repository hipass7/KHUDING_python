# Puyo Puyo
from collections import deque

graph = [list(map(str, input())) for _ in range(12)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

score = 0
while True:
    rest = False
    queue = deque([])
    visited = [[0] * 6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            cnt = 0
            if graph[i][j] == '.':
                continue
            if graph[i][j] != '.' and visited[i][j] == 0:
                queue = deque([(i, j)])
                restore = [(i, j)]
                while queue:
                    x, y = queue.popleft()
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]

                        if nx < 0 or ny < 0 or nx > 11 or ny > 5:
                            continue

                        if graph[nx][ny] == graph[x][y] and visited[nx][ny] == 0:
                            cnt += 1
                            queue.append((nx, ny))
                            visited[nx][ny] = 1
                            restore.append((nx, ny))

                if cnt >= 4:
                    for x, y in restore:
                        graph[x][y] = '.'
                    rest = True

    if not rest:
        break
    else:
        score += 1

    # 여기서 내려가는거 구현 해야함
    for j in range(6):
        cnt = 0
        for i in range(11,-1,-1):
            if graph[i][j] == '.':
                cnt += 1
                continue
            else:
                if cnt > 0:
                    graph[i+cnt][j] = graph[i][j]
                    graph[i][j] = '.'

print(score)