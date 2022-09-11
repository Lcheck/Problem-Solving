# 수열 A의 증가 부분 수열 중 합이 가장 큰 것 찾기


#테이블에는 현재 원소까지의 가장 큰 증가하는 부분수열합을 기록한다.
#테이블 n값은 수열 n값보다 작은 수열값 중에 제일 큰 테이블값에 수열 n 값을 더한 것이다. 

N=int(input())
nums=[0]+list(map(int,input().split(' ')))
#one-based-index
table=nums[:]
#만일 수열 n값보다 작은 수열값이 없다면 자기 자신이
#현재 원소까지의 가장 큰 증가하는 부분수열합일 수 있기 때문에 위와 같이 구성한다.

maxSum=0
maxSumIdx=0

for idx in range(1,N+1):
    maxSum=0
    maxSumIdx=0
    for pointer in range(1,idx): #수열 n값 왼쪽 수열들 순회
        if nums[pointer]<nums[idx] and table[pointer]>maxSum: #수열 n값보다 작은 수열값중에 제일 큰 테이블 값구하기 
           maxSum=table[pointer]
           maxSumIdx=pointer                          
    table[idx]+=table[maxSumIdx]
    #수열 n값보다 작은 수열 값이 없다면 0이 더해진다.
print(max(table))