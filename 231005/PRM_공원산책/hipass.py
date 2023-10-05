def solution(park, routes):
    fu = False
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "S":
                start = [i, j]
                fu = True
                break
        if fu:
            break
    
    for _ in routes:
        orig_start = start[:]
        for repeat in range(int(_[2])):
            if _[0] == "E":
                start[1] += 1
            elif _[0] == "S":
                start[0] += 1
            elif _[0] == "W":
                start[1] -= 1
            else:
                start[0] -= 1
            try:
                if park[start[0]][start[1]] == "X" or start[0] < 0 or start[1] < 0:
                    start = orig_start[:]
                    break
            except:
                start = orig_start[:]
                break
            
    answer = start 
    return answer
