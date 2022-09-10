# N에 사용할 수 있는 연산 (1,2는 나눠지는 경우만 사용가능)
# 3으로 나눈다
# 2로 나눈다
# 1을뺀다

# 위 연산들을 사용해서 N을 1로 만들어야함
# 최소 연산 횟수 출력
# 연산 과정 출력

#완전탐색X

#n-1의 최소연산 -> n의 최소연산
#2차원 배열로 한뒤 각배열의 첫째 원소에는 최소연산을, 둘째 원소에는 n-1의 인덱스를 기록한다
#->DP역추적

import sys

ipt = sys.stdin.readline
N=int(ipt())
table=[[0,0] for _ in range(N+10)]

table[1][0]=0
table[2][0]=1
table[2][1]=1
table[3][0]=1
table[3][1]=1
#table[4][0]=min(table[4//2][0],table[4-1][0])
#table[4][1].extend(table[2][0])

def findOper(n,types,preMinOperValue):
    for type in types: #이전 최소 연산 값의 연산 과정을 찾는다
         if table[type][0]==preMinOperValue: #해당 type이 최소연산의 index라면
            table[n][1]=type #index를 현재의 기록란에 기입한다. 
   

for n in range(4,N+1):
    types=[n-1,n//2,n//3]
    if n%2==0 and n%3==0: #2와 3 둘다 나눠지는 경우
       preMinOperValue=min(table[types[0]][0],table[types[1]][0],table[types[2]][0])#이전 최소 연산 값 찾기
       findOper(n,types,preMinOperValue)

    elif n%2==0 and n%3!=0: #2로만 나눠지는 경우
        preMinOperValue=min(table[types[0]][0],table[types[1]][0])
        del types[2] #findOper이용시 분기처리 못해서 미리 제거해둔다.
        findOper(n,types,preMinOperValue)

    elif n%2!=0 and n%3==0: #3으로만 나눠지는 경우
       preMinOperValue=min(table[types[0]][0],table[types[2]][0])
       del types[1]
       findOper(n,types,preMinOperValue)
    else:
       del types[2]
       del types[1] 
       preMinOperValue=table[types[0]][0]
       findOper(n,types,preMinOperValue)
    table[n][0]=preMinOperValue+1 #이전 최소 연산 값에 1을 더한게 현재 최소 연산 값

print(table[N][0])
print(N,end=' ')
while True:
      if N==1:break
      print(table[N][1],end=' ')
      N=table[N][1]



