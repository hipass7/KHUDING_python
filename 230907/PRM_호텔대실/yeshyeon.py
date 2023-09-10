# 시작시간 기준으로 정렬부터 한 뒤에, 차례대로 하나씩 비교하기
# dict 만들어서 dict에 저장되어 있는 end 시간과 현재 start 타임을 비교하기
# dict에 있는 end + 10분 값보다 start가 크거나 같으면 dict를 새로운 end로 변경

def timeChange(time):
    a = time.split(':');
    return (int(a[0]) * 60) + int(a[1])

def solution(book_time):
    answer = 0
    dicti = {}
    
    sortBookTime = sorted(book_time, key=lambda x:x[0])
    
    dicti[0] = 0
    
    breaker = False
    for i in sortBookTime :
        breaker = False;
        start = timeChange(i[0])
        end = timeChange(i[1])
        for key, value in dicti.items():
            if start >= (value+10) :
                dicti[key] = end
                breaker = True;
                break
                
        # 딕셔너리중 가장 마지막 키 값에서 +1 더한 값
        if breaker == False :
            dicti[list(dicti.keys())[-1]+1] = end
        
    answer = len(dicti.keys())
    
    return answer