# 입력
A, B = map(int, input().split())

N, M = map(int, input().split())
robots = [[-1, -1, "X"] for _ in range(N)] # 초기지점 및 바라보는 방향
commands = [[-1, "X", -1] for _ in range(M)] # 로봇번호, 움직이는 것, 반복횟수

for n in range(N):
    x, y, d = map(str, input().split())  # 문자열로 방향 받음
    robots[n] = [int(x), int(y), d]

for m in range(M):
    robot, move, repeat = map(str, input().split())
    commands[m] = [int(robot), move, int(repeat)]



# 로봇마다 우측 상단 지점이 기준점이 된다.

directions = ["N", "E", "S", "W"]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
crash = False

for c in commands:
    robot_num = c[0] #실제번호
    robot = robots[robot_num - 1] #인덱스 기준
    d = robot[2]
    ind = directions.index(d) #방향의 인덱스 0 = N, ...

    for _ in range(c[2]): # 반복횟수
        if c[1] == "L": 
            robot[2] = directions[(ind - 1) % 4]
            # print(robot_num, robot[2])

        elif c[1] == "R":
            robot[2] = directions[(ind + 1) % 4]
            # print(robot_num, robot[2])

        else:
            x, y, d = robot
            nx, ny = x + dx[ind], y + dy[ind]
            if nx < 1 or ny < 1 or nx > A or ny > B:
                # print(robot_num, nx, ny)
                print(f"Robot {robot_num} crashes into the wall")
                crash = True
                break
            new_list = [[robot[0], robot[1]] for robot in robots]
            if [nx, ny] in new_list:
                index = new_list.index([nx, ny])
                # print(robot_num, nx, ny)
                print(f"Robot {robot_num} crashes into robot {index+1}")
                crash = True
                break
            robot[0], robot[1] = nx, ny
            # print(robot_num, nx, ny)
    if crash:
        break
if not crash:
    print("OK")




