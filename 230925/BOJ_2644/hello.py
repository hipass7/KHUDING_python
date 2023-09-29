
n = int(input())
graph = [[] for _ in range(n+1)] # 1부터 n까지 나타내려면 n+1개를 만들어야 함
visited = [-1 for _ in range(n+1)] # n번 노드를 들렸는지? -> 안들렸으면 -1, 들렸으면 1로 초기화
start, end = map(int, input().split())
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y) # 인덱스에 해당하는 노드에 연결된 노드를 담는다. 
    graph[y].append(x)  

count = 0
def search(location, count):
    visited[location] = 1
    if location == end:
        return count  # 목표 노드에 도달했을 때 count 반환
    
    result = 0  

    for i in graph[location]:
        if visited[i] == -1:
            result = search(i, count + 1)  # count +1 해주면서 재귀 호출 -> 리턴값 result에 할당
            if result != 0: 
                break
    return result

count = search(start, count)  

if count == 0:
    print(-1)
else:
    print(count)
            
            
