# n개의 정수 수열이 주어짐
# '연속'된 수의 '합' 중 가장 '큰합'을 구할 것
# 수는 1개 이상선택


#테이블에는 N번째 원소 까지의 연속합을 저장한다.
#N번째 원소의 연속합은 N-1번째 원소 까지의 연속합 + N번째 원소값
#혹은 N번째 원소값이다.

#idea -처음부터 끊이지 않고 계속 더하는게 큰값을 만드는 방법이다.
#그러나 음수가 존재하기 때문에, 더하는 게 독이 될 수도 있다.
#끊이지 않고 합을 누적해 가되, 음수를 더해 값이 더 작아질 것 같으면
#끊고, N번째 원소를 저장한다. 

table=[-1001]*100005
N=int(input())
nums=list(map(int,input().split(' ')))
table[0]=nums[0]

for idx in range(1,N):
    table[idx]=max(table[idx-1]+nums[idx],nums[idx])

print(max(table))










