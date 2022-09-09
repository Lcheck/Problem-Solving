# n개의 정수 수열이 주어짐
# '연속'된 수의 '합' 중 가장 '큰합'을 구할 것
# 수는 1개 이상선택


# 1.n번째 원소의 모든 연속합을 구해 테이블에 저장한다. n=1
# 2.n+1번째 원소의 모든 연속합은 테이블의 각 원소에서 n번째 원소를 빼면 된다.

sums=[]
maxSums=[]
N=int(input())
nums=list(map(int,input().split(' ')))
sum=0

for i in nums:
    sum=sum+i
    sums.append(sum)
#n번째 원소를 포함한 연속합 n=1
maxSums.append(max(sums))

#n번째 원소를 포함한 가장 큰 연속합 저장


for num in nums[:len(nums)-2]:
        #마지막 원소 하나가 연속값인 경우가 있으므로 제외.
    for idx in range(len(sums)):
        sums[idx]-=num
    #n번째 원소를 포함한 연속합에서 n번째 원소의 값을 뺌
    #== n+1번째 원소를 포함한 연속합
    sums.pop(0)
    #연속합의 1번째 원소는 0이므로 삭제
    maxSums.append(max(sums))
    #n+1번째 원소를 포함한 가장 큰 연속합 저장


print(max(maxSums))
#가장 큰 연속합






