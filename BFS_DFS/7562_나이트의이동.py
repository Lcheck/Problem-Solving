from collections import deque;

testCase=int(input())

xlist=[1,-1,2, 2, 1,-1, -2,-2]
ylist=[2, 2,1,-1,-2,-2,  1,-1] #나이트 범위 좌표
result=[]

def bfs(nowX,nowY,futureX,futureY):
    
    visit[nowY][nowX]=1 #처음 밟은 곳 방문처리
    queue.append((nowY,nowX)) #처음 밟은 곳의 좌표 큐에 넣기

    while queue:  #큐가 빌 때 까지
        y,x=queue[0]        
        queue.popleft()    
              #큐에 들어있는 가장 첫번 째 원소 꺼내기

        if x==futureX and y==futureY: #만일 목표한 좌표에 도착했다면
            result.append(stage[y][x])
            break

        for i in range(8): # 나이트 방향 탐색
             X=x+xlist[i]
             Y=y+ylist[i]
         
             if X>=0 and X<length and Y>=0 and Y<length and visit[Y][X]==-1: #INDEX 범위 처리, 방문 체크
                     
                     visit[Y][X]=1 #방문 표시
                     stage[Y][X]=stage[y][x]+1 #도달 횟수 카운팅
                     queue.append((Y,X)) #방문할 곳 큐에 넣기
  
for _ in range(testCase):
    queue=deque()
    visit=[]
    stage=[]

    length=int(input())
    nowX,nowY=map(int,input().split(' '))
    futureX,futureY=map(int,input().split(' '))

    for i in range(length):   
        visit.append([])
        for j in range(length):
            visit[i].append(-1)

    for i in range(length):   
        stage.append([])
        for j in range(length):
            stage[i].append(0)

    bfs(nowX,nowY,futureX,futureY)

for i in result:
    print(i)

