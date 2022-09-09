# 1~n 연속수를 스택에 push했다가 pop한 수를 늘어 놓아 수열을 만듬.
# push순서는 오름차순

# 임의의 수열이 주어졌을때 
# 위 방법으로 만들 수 있는지 구분
# 만들 수 있으면 push, pop 연산의 순서 출력


#push는 계속 큰값이 들어갈 수 밖에 없음.
#첫째 값 이전의 수들을 리스트에 담아두고 pop
#감소하는 경우
#pop한다
#증가하는 경우
#해당 수가 될 때 까지 push하다가 pop한다

n=0
maxValue=0
nums=[]
result=[]

for i in range(int(input())):
    nums.append(int(input()))
for i in range(1,nums[0]+1):
    result.append('+')
maxValue=nums[0]
result.append('-')



while n<len(nums)-1:
     if nums[n]>nums[n+1]: #감소하는경우
        if maxValue<nums[n]: #현재값이 최고값인가?
           maxValue=nums[n] #최고값이면 최고값 갱신
        result.append('-')
     else: #증가하는경우
        for _ in range(nums[n+1]-maxValue):
            #증가한만큼 push
            maxValue+=1 #최고값도 1증가한다
            result.append('+')
        #하고 pop
        result.append('-')
     n=n+1
     

count=0
simulation=[]
compareResult=[]

#검증
for i in result:
    if i=='+':
       count+=1
       simulation.append(count)
    else:
       compareResult.append(simulation.pop())
       #pop할때에만 수열이 만들어진다

if nums!=compareResult:
   print('No')
else:
   for i in result:
       print(i)