# 그래프를 bfs와 dfs로 탐색한 결과를 출력
# 정점 번호가 작은 것을 번저 방문
# 방문할 수 있는 정점이 없는 경우 종료
# 정점 번호는 1~N
# 양방향 그래프

from collections import deque;

N,M,V=map(int,input().split(' '))
graph=[[0]for _ in range(N)]
graph.insert(0,[])
#one-indexed

for _ in range(1,M+1): 
    
    node,adjNode=map(int,input().split(' '))
    graph[node].append(adjNode)
    graph[adjNode].append(node)#양방향 그래프
    
#인접행렬로 데이터 가공


for i in range(1,N+1):   
    graph[i].sort()
#방문기준은 노드 번호가 낮은 순으로
    

def bfs(start):
    visit=[False for _ in range(0,N+1)]
    queue=deque()
    queue.append(start) #시작 정점을 큐에 넣는다.
    visit[start]=True; #동시에 방문 처리
    while queue: #큐가 빌 때 까지 반복한다.
         node=queue.popleft() #큐에서 정점을 꺼낸다.
         print(node,end=' ')

         for adjNode in graph[node][1:]: #인접 노드를 순회한다.
             if visit[adjNode]==False: #만일 방문 하지 않은 곳이라면
                queue.append(adjNode) #큐에 넣는다 == 방문한다
                visit[adjNode]= True #방문 처리를 미리 해둔다.
                #여기서 하지 않고 꺼낼 때 하게되면, 큐가 꼬인다


visit=[False for _ in range(0,N+1)]
stack=[]
#global

def dfs(now):
    print(now,end=' ')

    stack.append(now) #현재 정점을 스택에 넣는다

    if not stack: #스택이 빈 경우 중단한다.
       return
    
    visit[now]=True; #현재 정점을 방문처리한다.

    for adjNode in graph[now][1:]: #현 정점의 인접 노드를 순회한다
        if visit[adjNode]==False: #방문하지 않은 곳이면
           dfs(adjNode) #해당 정점으로 이동한다
           stack.pop() #호출 스택의 순서가 되면 pop된다

dfs(V)
print('')
bfs(V)

