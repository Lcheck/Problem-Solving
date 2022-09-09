# n개의 정수 수열이 주어짐
# '연속'된 수의 '합' 중 가장 '큰합'을 구할 것
# 수는 1개 이상선택


# 1.n번째 원소의 최대연속합을 구해 테이블에 저장한다. n=1
# 2.n+1번째 원소의 최대연속합은 n번째 원소의 최대연속합에서 n번째 원소를 뺀 것
# 만약 n번째 원소의 최대연속합이 n번째 원소인 경우 1로 돌아감

sums=[]
sum=0
maxSums=[-1001]*100001
N=int(input())
nums=list(map(int,input().split(' ')))

for i in nums:
    sum=sum+i
    sums.append(sum)
#n번째 원소의 연속합 n=1

maxSums[0]=max(sums)
#n번째 원소의 가장 큰 연속합 저장

for idx,num in enumerate(nums[:-2]):
        #마지막 원소 하나가 연속합인 경우가 있으므로 제외.
    if maxSums[idx]==num:
       # 만약 n번째 원소의 최대연속합이 n번째 원소인 경우
       sum=0
       sums=[]
       for i in nums[idx+1:]:
           sum=sum+i
           sums.append(sum)
       maxSums[idx+1]=max(sums)
       
       # n+1번째 원소의 최대 연속합을 완전탐색
    else:
       maxSums[idx+1]=maxSums[idx]-num
    #n+1번째 원소의 최대 연속합은 n번째 원소의 최대연속합에서 n번째 원소를 뺀 것

print(max(maxSums))
#가장 큰 연속합






