'''
Input
1. 세로 길이, 가로 길이
2. 행 별 블록 높이

Output
1. 고이는 빗물의 총량
'''

# H, W 입력 받아서 W * H 크기의 arr 선언
H, W = map(int, input().split())
arr = [[0 for x in range(W)] for y in range(H)]

# 블록 높이 입력 받아서 arr에 1로 블록 표시
block = list(map(int, input().split()))
for x in range(W) :
    for y in range(H) :
        if H-y <= block[x] :
            arr[y][x] = 1

# arr를 순환하며
# 각 열에서 1부터 1까지 사이의 빈 칸을 더해 temp에 저장 후 cnt에 합산
cnt = 0
for y in range(H) :
    state = 0
    temp = 0
    for x in range(W) :
        if state == 0 : 
            if arr[y][x] == 1 :
                state = 1
        else : # state == 1
            if arr[y][x] == 0 :
                temp += 1
            else : # state = 1
                cnt += temp
                temp = 0

print(cnt)
