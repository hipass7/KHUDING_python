def move(x, y, directions, R, C, matrix):
    direction_list = [1, 2, 3, 4]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    count = 0
    start = 0
    stop = 0

    while stop < 4:
        d = directions[start]
        i = direction_list.index(d)
        
        while True:
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and matrix[nx][ny] == '*':
                count += 1
                stop = 0
                matrix[nx][ny] = count
                x, y = nx, ny
                print(matrix) # 움직일때마다
            else:
                print("부딪혔다")
                stop += 1
                break
        start = (start + 1) % len(directions)  
    return (x, y)


# 입력받기
R, C = map(int, input().split())
matrix = [['*'] * C for _ in range(R)]
k = int(input())
obs = [[-1, -1] for _ in range(k)]
for i in range(k):
    br, bc = map(int, input().split())
    obs[i] = [br, bc]
sr, sc = map(int, input().split())
location = (sr, sc)
directions = [int(x) for x in input().split()]

# 초기 행렬 완성
for o in obs:
    matrix[o[0]][o[1]] = 'x'
matrix[sr][sc] = 0

location = move(location[0], location[1], directions, R, C, matrix)

print(*location)
