# 둘이서 숫자게임
# 어떤 정수 N개가 주어진다.
# 이 정수들을 K번까지 맘대로 나열한다.
# 그리고 그합을 구해 1,2,3,4 . . .를 만든다.
# 이것을 번갈아가며 진행한다.
# K번 이내에 수를 만들지 못하면 패배한다
# 사용하는 정수엔 1이 반드시 포함된다.

# 정수1,3  제한 5회
# 홀1짝11홀3짝13홀113짝33홀133짝1133


# 그리디 FAIL
# -> 거스름돈 문제는 그리디로 최적해 X


# 1~1000 까지 그리디로 각 숫자에 현재 정수들로 거스름돈을 거슬러준다.
# 한번씩 뺄셈 할 때 카운트를 세준다. 카운트가 K를 넘으면 멈춘다.

# N=int(input())
# choiceNums=list(map(int,input().split(' ')))
# choiceNums.sort(reverse=True)
# result=[]
# K=int(input())


# for n in range(1,1000*K):
#     num=n
#     idx=0
#     count=0
#     for _ in range(1,n+1):
#         if num>=choiceNums[idx]:
#            num=num-choiceNums[idx]
#            count+=1
#         else: 
#             idx+=1
#         if num<=0:
#            result.append((n,count))
#            break

# for t in result:
#     if t[1]==K+1:
#        winOrder=t[0]
#        break

# winner='holsoon' if winOrder%2==0 else 'jjaksoon'
# print(f'{winner} win at {winOrder}')


# .. FAIL

# N=int(input())
# choiceNums=list(map(int,input().split(' ')))
# K=int(input())
# winOrder=max(choiceNums)*K-1
# winner='holsoon' if winOrder%2==0 else 'jjaksoon'
# print(f'{winner} win at {winOrder}')


#DP + visitting

# 각 테이블의 인덱스는 덧셈의 횟수 (1~k)
# 각 테이블의 값은 해당 횟수로 만들어 질 수 있는 모든 값들
# 점화식 -> dp[n]=dp[n-1]의 각 원소에 모든 원소들을 더해본 값들(이미 더한 것은x)
#3
#1 2 5
#5
# dp[1]=[1,2,5]
# dp[2]=[2,3,6,4,7,10]

#K인덱스 까지의 dp테이블의 값들을 visit 체크한다.
#처음으로 False가 되어 있는 곳은 K까지의 횟수로 만들지 못한 수이므로
#해당 수에서 패배한 것이다.

N=int(input()) #숫자의 개수
choiceNums=list(map(int,input().split(' '))) #주어진 숫자들
K=int(input()) #조합 제한 횟수

visit=[0]+[False for _ in range(1000)] #방문 체크용
dp=[0]+[[] for _ in range(1000)] #dp 테이블
dp[1]=choiceNums #1회로 만들 수 있는 모든 값들

for n in range(2,K+1): #dp 테이블 만들기
    dp[n]=set(dp[n]) #중복 제거를 위한 set 사용
    for num in set(dp[n-1]):
        for cNum in choiceNums:
            dp[n].add(num+cNum)

for i in range(1,K+1): #테이블 이용해 방문 체크 하기
    for k in dp[i]:
        visit[k]=True

for i in range(1,len(visit)): #False 검사
    if not visit[i]:
       winOrder=i
       winner='holsoon' if winOrder%2==0 else 'jjaksoon'
       break
print(f'{winner} win at {winOrder}')