# n을 최소 개수의 제곱수 합으로 표현
# 최소가 되는 제곱수의 개수 구하기

#그리디?

#n을 구성할 수 있는 가장 큰 제곱수를 구한다
#n=n-가장 큰 제곱수
#제곱수의 합이 n이 될 때 까지 반복
# --> 최적해 X

#DP

# 1 1              1
# 2 1 1            2
# 3 1 1 1          3
# 4 2              1

# 5 2 1            2
# 6 2 1 1          3
# 7 2 1 1 1        4
# 8 2 2            2
# 9 3              1

# 10 3 1           2
# 11 3 1 1         3
# 12 2 2 2         3
# 13 3 2           2
# 14 3 2 1         3
# 15 3 2 1 1       4
# 16 4             1

# 17 4 1           2
# 18 3 3           2
# 19 3 3 1         3
# 20 4 2           2
# 21 4 2 1         3
# 22 3 3 2         3
# 23 3 3 2 1       4

# if 현재수 - 최대 제곱수 == 0:
#    dp[현재수]=1
# dp[현재수]= min(dp[현재수 - 최대 제곱수] ,dp[현재수 - 최대 제곱수 -1] , dp[현재수 - 최대 제곱수 - n ] ... ) +1

import sys
input = sys.stdin.readline

N=int(input())
table=[0 for i in range(N+5)]

table[1]=1
table[2]=2
table[3]=3
table[4]=1

if N<=4:
   print(table[N])
   exit()

for i in range(5,N+2):
    temp=[]
    maxSq=int(i**0.5)
    # table[i]=9999999 #table[i]의 초기 값은 0이므로 첫 비교시 최대치로 설정
    for k in range(2,maxSq+1):
        # table[i]=min(table[i],table[i-k**2]+1) #매번 비교하며 갱신하는 방법 (최적화)
        temp.append(table[i-k**2])
    table[i]=min(temp)+1

print(table[N])

#pypy로 제출해야 시간초과 안남

