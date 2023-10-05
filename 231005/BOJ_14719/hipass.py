# 빗물

h, w = map(int, input().split())
graph = list(map(int, input().split()))

total = 0
for i in range(h):
    water = False
    cnt = 0
    for j in range(w):
        if graph[j] > i:
            if water == False:
                water = True
            else:
                total += cnt
                cnt = 0

        if graph[j] <= i:
            if water:
                cnt += 1
                continue

print(total)
