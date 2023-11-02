from collections import deque

n, w, L = map(int, input().split())
a = list(map(int, input().split()))

time = 0
sum = 0
i = 0

bridge = deque()
for _ in range(w) :
    bridge.append(0)

passed_truck = 0

# 통과한 트럭의 수가 n일 될 때까지 반복
while passed_truck < n :
    x = bridge.popleft()
    sum -= x

    # 도착지에 도착한 값이 0이 아니면 트럭
    if x != 0 :
        passed_truck += 1

    # 트럭이 다리에 들어갈 수 있으면 입장
    if i < n and sum + a[i] <= L :
        bridge.append(a[i])
        sum += a[i]
        i += 1
    # 트럭이 다리에 들어갈 수 없으면 0으로 채우기
    else :
        bridge.append(0)

    time += 1

print(time)
