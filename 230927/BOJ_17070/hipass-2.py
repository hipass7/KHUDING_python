# 파이프 옮기기
from collections import deque

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

def rkfh(x, y):
    nx = x
    ny = y + 1
    try:
        if graph[nx][ny] == 1:
            pass
        else:
            graph[nx][ny] -= 1
            queue.append((nx, ny, 0))
    except:
        pass

    nx += 1
    try:
        if graph[nx][ny] == 1 or graph[nx][ny-1] == 1 or graph[nx-1][ny] == 1:
            pass
        else:
            graph[nx][ny] -= 1
            queue.append((nx, ny, 2))
    except:
        pass

def tpfh(x, y):
    nx = x + 1
    ny = y
    try:
        if graph[nx][ny] == 1:
            pass
        else:
            graph[nx][ny] -= 1
            queue.append((nx, ny, 1))
    except:
        pass

    ny += 1
    try:
        if graph[nx][ny] == 1 or graph[nx-1][ny] == 1 or graph[nx][ny-1] == 1:
            pass
        else:
            graph[nx][ny] -= 1
            queue.append((nx, ny, 2))
    except:
        pass

def eorkrtjs(x, y):
    nx = x
    ny = y + 1
    try:
        if graph[nx][ny] == 1:
            pass
        else:
            graph[nx][ny] -= 1
            queue.append((nx, ny, 0))
    except:
        pass

    nx += 1
    ny -= 1
    try:
        if graph[nx][ny] == 1:
            pass
        else:
            graph[nx][ny] -= 1
            queue.append((nx, ny, 1))
    except:
        pass

    ny += 1
    try:
        if graph[nx][ny] == 1 or graph[nx-1][ny] == 1 or graph[nx][ny-1] == 1:
            pass
        else:
            graph[nx][ny] -= 1
            queue.append((nx, ny, 2))
    except:
        pass

queue = deque([(0, 1, 0)])

while queue:
    x, y, d = queue.popleft()
    if d == 0:
        rkfh(x, y)
    elif d == 1:
        tpfh(x, y)
    else:
        eorkrtjs(x, y)


result = -graph[n-1][n-1]
if result > 0:
    print(result)
else:
    print(0)

# 완전 탐색으로 풀이 시 python 특성 상 시간초과