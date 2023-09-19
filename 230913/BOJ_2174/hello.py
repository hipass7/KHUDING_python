
# 입력
A, B = map(int, input().split())

N, M = map(int, input().split())
robots = [[-1, -1, "X"] for _ in range(N)] # 초기지점 및 바라보는 방향
commands = [[-1, "X", -1] for _ in range(M)] # 로봇번호, 움직이는 것, 반복횟수
directions = {'N': 0, 'E': 1, 'S': 2, 'W': 3}

for n in range(N):
    x, y, d = map(str, input().split())  # 문자열로 방향 받음
    robots[n] = [int(x), int(y), directions[d]]

for m in range(M):
    robot, move, repeat = map(str, input().split())
    commands[m] = [int(robot), move, int(repeat)]



# 로봇마다 우측 상단 지점이 기준점이 된다.


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
crash = False

for c in commands:
    robot_num = c[0] #실제번호
    

    for _ in range(c[2]): # 반복횟수
        x, y, d = robots[robot_num - 1]
        new_list = [[robot[0], robot[1]] for robot in robots]
        print(robot_num, x, y, d)

        if c[1] == "L": 
            d = (d-1)%4
            robots[robot_num - 1] = x, y, d

        elif c[1] == "R":
            d = (d+1)%4
            robots[robot_num - 1] = x, y, d

        else:
            nx, ny = x + dx[d], y + dy[d]
            if nx < 1 or ny < 1 or nx > A or ny > B:
                print(f"Robot {robot_num} crashes into the wall")
                crash = True
                break
            
            if [nx, ny] in new_list:
                index = new_list.index([nx, ny])
                print(f"Robot {robot_num} crashes into robot {index+1}")
                crash = True
                break
            x, y = nx, ny
            robots[robot_num - 1] = (x, y, d)
    if crash:
        break
if not crash:
    print("OK")