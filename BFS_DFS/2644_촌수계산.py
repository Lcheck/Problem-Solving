

from collections import deque;


pCount=int(input())
p1,p2=map(int,input().split(' '))
parentChildCount=int(input())

graph=[[0]for _ in range(pCount)]
graph.insert(0,[])
#one-indexed

for _ in range(parentChildCount): 
    
    node,adjNode=map(int,input().split(' '))
    graph[node].append(adjNode)
    graph[adjNode].append(node)#양방향 그래프
    
#인접행렬로 데이터 가공


for i in range(1,pCount+1):   
    graph[i].sort()
#방문기준은 노드 번호가 낮은 순으로
    

def bfs(start):
    queue=deque()
    count=0
    queue.append(start) #시작 정점을 큐에 넣는다.
    visit[start]=0; #동시에 방문 처리
    while queue: #큐가 빌 때 까지 반복한다.
         node=queue.popleft() #큐에서 정점을 꺼낸다.
         count+=1
         for adjNode in graph[node][1:]: #인접 노드를 순회한다.
             if visit[adjNode]==-1: #만일 방문 하지 않은 곳이라면
                queue.append(adjNode) #큐에 넣는다 == 방문한다
                visit[adjNode]= visit[node]+1 #방문 처리와 동시에 이동 횟수를 기록한다.
                #여기서 하지 않고 꺼낼 때 하게되면, 큐가 꼬인다


visit=[-1 for _ in range(0,pCount+1)]
stack=[]
#global


bfs(p1)

print(visit[p2])

#맞았지만 왜 시작 지점의 이동횟수가 0이 아니게 되는지 의문임