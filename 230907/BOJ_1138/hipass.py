# 이런식으로 본인닉네임.py 로 만들어서 만들죠! 폴더는 제가 문제 선정하면 바로 만들어두겠습니다.

n = int(input())
graph = list(map(int, input().split()))

result = [0] * n

for _ in range(n):
    cnt = graph[_]
    for i in range(n):
        if cnt == 0:
            if result[i] != 0:
                continue
            result[i] = _+1
            break
        if result[i] == 0:
            cnt -= 1
        
print(*result)