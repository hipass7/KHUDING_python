# 촌수계산

from collections import deque

n = int(input())
a, b = map(int, input().split())

a -= 1
b -= 1

graph = [[0] * n for _ in range(n)]
visited = [0] * n
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    graph[x][y] = 1
    graph[y][x] = 1

queue = deque()
queue.append(a)
result = []
cnt = 0
visited[a] = 1
ox = False
while queue:
    temp = queue.popleft()
    result.append(temp)
    if temp == b:
        ox = True
        break
    for i in range(n):
        if graph[temp][i] == 1 and visited[i] == 0:
            queue.append(i)
            visited[i] = visited[temp] + 1

    
if not ox:
    print(-1)
else:
    print(visited[b] - 1)