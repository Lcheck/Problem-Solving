from collections import deque;

nodeCount=int(input())
edgeCount=int(input())

edges=[]
parentList=list(range(0,nodeCount+1))

for _ in range(edgeCount): 
    
    node,adjNode=map(int,input().split(' '))
    edges.append((node,adjNode))#무방향그래프
   

def getParent(nodeIndex):
    if parentList[nodeIndex]==nodeIndex: #연결되지 않아서 자기자신이 부모일 때
        return parentList[nodeIndex]

    parentList[nodeIndex]=getParent(parentList[nodeIndex])  #재귀적으로 부모 찾기 (인덱스와 값이용) -> 이때 자기 자신의 부모가 갱신된다 그러나 후반부에 union이 발생하는경우
    #부모 갱신이 안될 수도 있기 때문에 마지막에 모든 정점을 getParent해주어야 함

    return  parentList[nodeIndex] #부모 반환


def union(nodeIndex1,nodeIndex2):
    one=getParent(nodeIndex1)   #두 정점의 부모 확인 
    two=getParent(nodeIndex2)
    if one<two:                       #큰쪽의 부모를 작은 쪽의 부모로 종속
        parentList[two]=one
    else:
        parentList[one]=two


def find(nodeIndex1,nodeIndex2):     # 두 정점의 부모가 같은지 확인
    a=getParent(nodeIndex1)
    b=getParent(nodeIndex2) 
 
    if a==b:
       return 1
    else:
       return 0  

for i in edges:                 
    if i[0]==i[1]:     #경로가 없는 경우 제외
        continue
    if find(i[0],i[1])==0:    # 두 정점의 부모가 같지않으면
       union(i[0],i[1])   #합한다

for i in range(nodeCount+1):
    getParent(i)  #부모 다시 한번 갱신해주기

print(parentList.count(1)-1) #1과 연결되어 있는 정점의 개수 반환
