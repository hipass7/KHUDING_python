# 방번호

num = input()

graph = [0] * 10
for _ in num:
    graph[int(_)] += 1

graph[6] += graph[9]
graph[6] /= 2
graph[9] = 0

print(round(max(graph)+0.1))