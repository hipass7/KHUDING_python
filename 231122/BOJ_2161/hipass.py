# 카드1
from collections import deque

n = int(input())

queue = deque([])
result = []
for _ in range(n):
    queue.append(_+1)

while queue:
    x = queue.popleft()
    result.append(x)
    if not queue:
        break
    y = queue.popleft()
    queue.append(y)

print(*result)


