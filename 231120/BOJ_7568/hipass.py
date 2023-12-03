# 덩치

n = int(input())
graph = []
result = []
for _ in range(n):
    x, y = map(int, input().split())
    graph.append((x,y))

for x, y in graph:
    cnt = 1
    for a, b in graph:
        if x < a and y < b:
            cnt += 1
        else:
            continue

    result.append(cnt)

print(*result)