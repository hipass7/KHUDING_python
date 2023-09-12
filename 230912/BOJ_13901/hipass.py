#test
R, C = map(int, input().split())
k = int(input())

graph = [[0] * C for _ in range(R)]
for _ in range(k):
    a, b = map(int, input().split())
    graph[a][b] = 1

sr, sc = map(int, input().split())

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

dd = list(map(int, input().split()))

graph[sr][sc] = 1


direction = 0
cnt = 0
while True:
    if cnt > 3:
        break
    if direction > 3:
        direction = 0
    x = sr + dx[dd[direction]]
    y = sc + dy[dd[direction]]
    if x < 0 or x >= R or  y < 0 or y >= C:
        direction += 1
        cnt += 1
        continue
    if graph[x][y] == 1:
        direction += 1
        cnt += 1
        continue


    sr += dx[dd[direction]]
    sc += dy[dd[direction]]
    graph[x][y] = 1
    cnt = 0

print(sr, sc)