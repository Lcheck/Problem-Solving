from collections import deque

def compare(deque,num): #큐안에 자신보다 중요도가 높은 문서가 있는지 알려주는 함수
    for i in deque:
        if i[0]>num:
            return True

for i in range(int(input())):
    N,M=map(int,input().split())
    nums=list(map(int,input().split())) 
    count=0

    tnums=deque()   #각 문서를 구별하기 위해 튜플 형태로 큐 구성
    for i in range(len(nums)):
        
        tnums.append((nums[i],i)) 

    while tnums:
        for i in list(tnums): #덱을 리스트화 해서 순회
            if compare(tnums,i[0]): #큐내에 자기보다 중요도가 큰 문서가 있으면
                tnums.append(tnums.popleft()) #후순위로 배치
            else: #없으면
                tnums.popleft() #출력
                count=count+1 #카운트 증가
                if i[1]==M:   #만일 목표 문서가 인쇄된 경우
                   print(count) #카운트 출력





