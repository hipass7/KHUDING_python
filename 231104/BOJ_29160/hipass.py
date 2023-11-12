# 팀 가치

N, K = map(int, input().split())

graph = []
grade = [0] * 11
idx = [0] * 11
for members in range(N):
    x, y = map(int, input().split())
    graph.append([x, y])

for year in range(K):
    for i in range(N):
        if grade[graph[i][0] - 1] < graph[i][1]:
            idx[graph[i][0] - 1] = i
            grade[graph[i][0] - 1] = graph[i][1]

    for i in idx:
        graph[i][1] -= 1

    grade = [0] * 11
    idx = [0] * 11

    for i in range(N):
        if grade[graph[i][0] - 1] < graph[i][1]:
            idx[graph[i][0] - 1] = i
            grade[graph[i][0] - 1] = graph[i][1]

print(sum(grade))

    