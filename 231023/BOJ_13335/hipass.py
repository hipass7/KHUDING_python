from collections import deque

n, w, L = map(int, input().split())
truck = list(map(int, input().split()))
trucks = deque(truck)

queue = deque([0] * w)
cnt = 0
truck_cnt = len(truck)
push = True

while queue:
    cnt += 1
    span = queue.popleft()
    if push:
        x = trucks.popleft()
    if (sum(queue) + x) <= L:
        queue.append(x)
        push = True
        if not trucks:
            break
    else:
        queue.append(0)
        push = False

print(cnt+w)