# {1:"ABACD", 2:"AABB"}
# targets를 반복문으로 돌면서 한 문자씩 확인 
# -> for문으로 하나씩 확인하기, 이중포문으로 "A" 
#-> for 문으로 keymap을 하나씩 탐색하고 index가 가장 낮은 것을 찾은 후 +1 하기

def solution(keymap, targets):
    answer = []
    
    dict = {};
    for idx, itm in enumerate(keymap) :
        dict[idx] = itm
    
    for idx, itm in enumerate(targets) :
        버튼클릭수 = 0;
        for idx2, itm2 in enumerate(itm) :
            minimumIdx = -1;
            for i in dict :
                # 만약 -1일때 (해당 딕셔너리 키에서 못찾았을때 다음 키로)
                if dict[i].find(itm2) == -1 :
                    continue
                # 만약 minimumIdx가 -1이 아닐 때는 dict.find한 인덱스 값 넣기
                if minimumIdx == -1 :
                    minimumIdx = dict[i].find(itm2)
                # 만약 minimumIdx가 -1 아니고, 이전 인덱스보다 작은 횟수로 클릭할 수 있으면 값 변경
                if minimumIdx > dict[i].find(itm2):
                    minimumIdx = dict[i].find(itm2)
            
            # 만약 어느 딕셔너리 키에서도 못찾았을때는 -1을 넣기, 한 문자를 못하면 글자 자체를 못만드니까 for 탈출
            if minimumIdx == -1 :
                버튼클릭수 = -1
                break;
            # 그렇지 않으면 버튼클릭수에 합산해나가고 그 다음 문자 1개 보기
            else:
                버튼클릭수 += minimumIdx + 1
            
        answer.append(버튼클릭수)

    return answer