#거스름돈을 2, 5원으로 구성해야함
#동전은 최소 갯수로
#13원인경우 5원이 2개면 안되므로 greedy X

#1, 3빼고는 다 거슬러 줄 수 있음

#거스름돈=테이블의 인덱스
#원소값은 최소 동전의 개수로한다.

N=int(input())

if N==1 or N==3:
   print(-1)
   exit()

table=[100001]*(N+5)
table[2]=1
table[4]=2
table[5]=1

for n in range(6,N+1):
    table[n]=min(table[n-2],table[n-5])+1
    #n의 값은 n-2와 n-5 중 최소동전개수가 더 작은 값에서 +1한 것과 같다.
print(table[N])







