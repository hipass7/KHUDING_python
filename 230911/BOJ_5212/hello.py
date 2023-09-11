def sinkLand(current_map, R, C):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    new_map = [['.'] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if current_map[i][j] == 'X':
                count = 0
                for k in range(len(dx)):
                    nx, ny = i + dx[k], j + dy[k]
                    if nx < 0 or ny < 0:
                        count += 1
                    else:
                        try:
                            if current_map[nx][ny] == '.': 
                                count += 1
                        except:
                            count += 1
                if count >= 3:
                    new_map[i][j] = '.'
                else:
                    new_map[i][j] = 'X'
    
    return new_map

R, C = map(int, input().split())
current_map = [list(input()) for _ in range(R)]

new_map = sinkLand(current_map, R, C)

min_x, max_x, min_y, max_y = R, -1, C, -1

for x in range(R):
    for y in range(C):
        if new_map[x][y] == 'X':
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)

for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        print(new_map[x][y], end='')
    print()
