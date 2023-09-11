#test

r, c = map(int, input().split())

graph = [list(map(str, input())) for _ in range(r)]

for i in range(r):
    for j in range(c):
        cnt = 0
        if graph[i][j] == '.':
            continue
        if i-1 < 0:
            cnt += 1
        elif graph[i-1][j] == '.':
            cnt += 1
        try:
            if graph[i+1][j] == '.':
                cnt += 1
        except:
            cnt += 1
        try:
            if graph[i][j+1] == '.':
                cnt += 1
        except:
            cnt += 1
        if j-1 < 0:
            cnt += 1
        elif graph[i][j-1] == '.':
            cnt += 1

        if cnt >= 3:
            graph[i][j] = 0

first = [11, 11]
last = [0, 0]
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'X':
            if first[0] > i:
                first[0] = i
            if first[1] > j:
                first[1] = j
            if last[0] < i:
                last[0] = i
            if last[1] < j:
                last[1] = j
        if graph[i][j] == 0:
            graph[i][j] = '.'

result_x = graph[first[0]:last[0]+1]

for _ in result_x:
    print(*_[first[1]:last[1]+1], sep='')