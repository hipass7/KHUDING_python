n, m = map(int, input().split())

field = [list(map(str, input())) for _ in range(n)]

rem = [0] * 11
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

for i in range(1,n-1):
    for j in range(1, m-1):
        if field[i][j] == 'R':
            R = [i, j]
        elif field[i][j] == 'B':
            B = [i, j]
        elif field[i][j] == 'O':
            O = [i, j]

queue = [[0, R, B]]

while queue:
    cnt, R, B = queue.pop(0)
    R_orig, B_orig, O_orig = R[:], B[:], O[:]
    cnt += 1
    if cnt > 10:
        break
    for k in range(4):
        temp = False
        R, B, O = R_orig[:], B_orig[:], O_orig[:]
        # init
        field[B[0]][B[1]] = 'B'
        field[O[0]][O[1]] = 'O'
        field[R[0]][R[1]] = '.'
        while field[R[0]][R[1]] == '.':
            if field[R[0]+dx[k]][R[1]+dy[k]] == '#' or field[R[0]+dx[k]][R[1]+dy[k]] == 'B':
                break
            R[0] += dx[k]
            R[1] += dy[k]
        if field[R[0]][R[1]] == 'O':
            pass
        else:
            field[R[0]][R[1]] = 'R'

        field[B[0]][B[1]] = '.'
        while field[B[0]][B[1]] == '.':
            if field[B[0]+dx[k]][B[1]+dy[k]] == '#' or field[B[0]+dx[k]][B[1]+dy[k]] == 'R':
                break
            B[0] += dx[k]
            B[1] += dy[k]
        if B != O:
            if R == O:
                rem[cnt] = True
                continue
        elif B == O:
            continue

        if B == R:
            if (abs(B[0] - B_orig[0]) + abs(B[1] - B_orig[1])) > (abs(R[0] - R_orig[0]) + abs(R[1] - R_orig[1])):
                B[0] -= dx[k]
                B[1] -= dy[k]
            else:
                R[0] -= dx[k]
                B[1] -= dy[k]

        field[B[0]][B[1]] = '.'

        field[R[0]][R[1]] = '.'
        if [cnt, R, B] not in queue:
            queue.append([cnt, R, B])


for i in range(len(rem)):
    if rem[i]:
        print(i)
        break
    elif i == len(rem) - 1:
        print(-1)
