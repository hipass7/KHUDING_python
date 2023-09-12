def move(x, y, direction, R, C, matrix, c):
    direction_list = [1, 2, 3, 4]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    i = direction_list.index(direction)
    nx, ny = x + dx[i], y + dy[i]

    if 0 <= nx < R and 0 <= ny < C and matrix[nx][ny] == '*':
        matrix[nx][ny] = c
        return (nx, ny)

    return (x, y)

#입력받기
R,C = map(int, input().split())
matrix = [['*'] * C for _ in range(R)]
k = int(input())
obs = [[-1, -1] for _ in range(k)]
for i in range(k):
    br, bc = map(int, input().split())
    obs[i] = [br, bc]
sr, sc = map(int, input().split())
location = (sr, sc)
directions = [int(x) for x in input().split()]

#초기 행렬 완성
for o in obs:
    matrix[o[0]][o[1]] = 'x'
matrix[sr][sc] = 0

#입력받은 방향순으로 iteration
for k in range(len(directions)):
    location = move(location[0], location[1], directions[k], R, C, matrix, k + 1)

print(matrix)
print(*location)