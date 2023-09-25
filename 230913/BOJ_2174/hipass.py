#test
A, B = map(int, input().split())
graph = [0] * A
N, M = map(int, input().split())

robots = []
for _ in range(N):
    x, y, d = map(int, input().split())
    if d == 'N':
        d = 0
    elif d == 'E':
        d = 1
    elif d == 'S':
        d = 2
    else:
        d = 3
    robots.append([x, y, d])

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(M):
    robot, order, rep = map(int, input().split())
    temp = robots[robot-1]
    for __ in range(rep):
        if order == 'L':
            temp[2] -= 1
        elif order == 'R':
            temp[2] += 1
        else:
            pass

# 문제풀이 중 hello.py의 문제풀이가 완벽하다고 생각하여 해당 코드를 갖고 code review 후 마무리