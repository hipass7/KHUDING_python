N = int(input())
matrix = []

for _ in range(N):
    matrix.append(list(map(int, input().split())))

dx = [0, 1, 0, -1] # NESW
dy = [-1, 0, 1, 0]

result = 0 # 안전영역 개수

height = -1 # 1 이상 100 이하 정수
while height <= 100: 
    height += 1
    visited = [[False] * N for _ in range(N)]
    area_count = 0  # height마다 0으로 초기화

    for i in range(N):
        for j in range(N):
            if not visited[i][j] and matrix[i][j] > height: # 이미 들린 곳은 안가도 됨
                stack = [(i, j)]  
                visited[i][j] = True
                area_count += 1  # 안전 영역 개수 증가

                while stack:
                    xx, yy = stack.pop()

                    for k in range(len(dx)):
                        nx, ny = xx + dx[k], yy + dy[k] # xx, yy 기준으로 사방 순환

                        if nx >= 0 and nx < N and ny >= 0 and ny < N and visited[nx][ny] == False and matrix[nx][ny] > height:
                            stack.append((nx, ny)) #스택에 추가
                            visited[nx][ny] = True # 사방 중 잠기지 않은 지역에 들렀다고 표시 남김

    result = max(result, area_count)  # 최대값 초기화

print(result)



