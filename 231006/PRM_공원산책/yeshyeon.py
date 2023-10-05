# N북 S남 W서 E동

def can_go_next(park, x, y):
    if x < 0 or y < 0 or x >= len(park) or y >= len(park[0]) or park[x][y] == 'X':
        return False
    else :
        return True

def solution(park, routes):
    
    # 현재위치
    current_x = 0
    current_y = 0
    
    # S 위치 찾기
    for v in range(len(park)) :
        if park[v].find('S') >= 0 :
            current_x = v
            current_y = park[v].find('S')
            break
    
    for i in routes:
        
        # 가려고 하는 위치
        future_x = current_x;
        future_y = current_y;
        
        if i[0] == 'E' :
            can_go = True;
            for count in range(1, int(i[2])+1) :
                future_y += 1
                can_go = can_go_next(park, future_x, future_y)
                if can_go == False :
                    break
            # 문제없이 갔다면 can_go가 여전히 True 일 것이니, 현재위치 변경
            if can_go :
                current_y = future_y
        
        elif i[0] == 'S' :
            can_go = True;
            for count in range(1, int(i[2])+1) :
                future_x += 1
                can_go = can_go_next(park, future_x, future_y)
                if can_go == False :
                    break
                    
            if can_go :
                current_x = future_x
                        
        elif i[0] == 'W' :
            can_go = True
            for count in range(1, int(i[2])+1) :
                future_y -= 1
                can_go = can_go_next(park, future_x, future_y)
                if can_go == False:
                    break
                    
            if can_go :
                current_y = future_y
                        
        elif i[0] == 'N' :
            can_go = True
            for count in range(1, int(i[2])+1) :
                future_x -= 1
                can_go = can_go_next(park, future_x, future_y)
                if can_go == False:
                    break
                    
            if can_go :
                current_x = future_x
            
    answer = [current_x, current_y]
    return answer