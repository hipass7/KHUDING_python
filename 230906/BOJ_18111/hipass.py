# 이런식으로 본인닉네임.py 로 만들어서 만들죠! 폴더는 제가 문제 선정하면 바로 만들어두겠습니다.

N, M, B = map(int, input().split())
B_origin = B
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

res_min = 987654321
idx = 0

for block in range(257):
    cnt = 0
    escape = False
    B = B_origin
    for i in graph:
        for j in i:
            if j > block:
                cnt += (j - block) * 2
                B += (j - block)
            else:
                cnt += (block - j)
                B -= (block - j)

    if B < 0:
        continue
    if cnt <= res_min:
        res_min = cnt
        idx = block
        continue

print(res_min, idx)