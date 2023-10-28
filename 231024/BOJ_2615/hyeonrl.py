px = [1, 0, 1, 1]
py = [0, 1, -1, 1]

winner = 0

board = [list(map(int, input().split())) for i in range(19)]

for y in range(19) :
    for x in range(19) :
        if board[y][x] != 0 :
            for p in range(4) :
                ex = x - px[p]
                ey = y - py[p]
                if ex >= 0 and ey >= 0 and ex < 19 and ey <19 and board[y][x] == board[y-py[p]][x-px[p]] :
                    continue

                xx = x + px[p]
                yy = y + py[p]

                cnt = 1
                while xx >= 0 and yy >= 0 and xx < 19 and yy < 19 and board[y][x] == board[yy][xx] :
                    xx += px[p]
                    yy += py[p]
                    cnt += 1
                if cnt == 5 :
                    winner = board[y][x]
                    wx, wy = x+1, y+1

print(winner)
if winner != 0 :
    print(wy, wx)
