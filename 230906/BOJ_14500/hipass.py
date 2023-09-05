class Poly:
    def __init__(self, shape):
        if shape == "blue":
            self.stack = [[[0, 0, 0],[1, 1, 1]], [[1, 1, 1], [0, 0, 0]]]
        elif shape == "yellow":
            self.stack = [[[1, 0, -1],[0, 1, 0]]]
        elif shape == "orange":
            self.stack = [[[1, 1, 0],[0, 0, 1]], [[-1, 0, 0], [0, 1, 1]], [[0, 1, 1], [1, 0, 0]], [[0, 0, -1], [1, 1, 0]],[[1, 1, 0], [0, 0, -1]], [[0, 0, 1], [1, 1, 0]], [[0, 1, 1],[-1, 0, 0]], [[1, 0, 0],[0, 1, 1]]]
        elif shape == "green":
            self.stack = [[[1, 0, 1], [0, 1, 0]], [[0, -1, 0], [1, 0, 1]], [[1, 0, 1], [0, -1, 0]], [[0, 1, 0], [1, 0, 1]]]
        else:
            self.stack = [[[0, 0, 1], [1, 1, -1]], [[-1, 1, 1], [1, 0, 0]], [[0, -1, 1], [1, 0, 1]], [[1, 1, -1], [0, 0, 1]]]

    
n, m = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
queue = [Poly("blue"), Poly("yellow"), Poly("orange"), Poly("green"), Poly("purple")]

total = []
validate = True
for i in range(n):
    for j in range(m):
        for mino in queue:
            for loc in mino.stack:
                cnt = graph[i][j]
                copy_i = i
                copy_j = j
                for idx in range(3):
                    copy_i += loc[0][idx]
                    copy_j += loc[1][idx]
                    if copy_i < 0 or copy_j < 0:
                        validate = False
                        break
                    try:
                        cnt += graph[copy_i][copy_j]
                    except:
                        validate = False
                        break
                if validate:
                    total.append(cnt)
                validate = True

print(max(total))