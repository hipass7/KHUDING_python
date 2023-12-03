# 올림픽

n, k = map(int, input().split())

graph = []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    if a == k:
        gold, silver, bronze = b, c, d
    else:
        graph.append((b, c, d))
    
cnt = 1
for x, y, z in graph:
    if x > gold:
        cnt += 1
        continue
    elif x == gold:
        if y > silver:
            cnt += 1
            continue
        elif y == silver:
            if z > bronze:
                cnt += 1
                continue

print(cnt)