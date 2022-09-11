# 수열 A의 증가 부분 수열 중 합이 가장 큰 것 찾기

# 각원소기준 작은 값들은 필요없다.

# 테이블에는 누적합이 적혀있다
# 수열n-1 보다 수열n이크면 테이블n의 값은 수열n값 +테이블n-1값이다.
# 작으면 테이블n-1에 수열n-1를 뺀고 수열n을 더한 것을 테이블n값으로 한다.

table=[0 for i in range(int(input())+5)]
nums=[0]
nums.extend(list(map(int,input().split(' '))))
table=nums[:]
#one-based-index

for idx in range(2,len(nums)):
    if nums[idx-1]<nums[idx]:
       table[idx]=table[idx-1]+nums[idx]

print(table)
print(max(table))