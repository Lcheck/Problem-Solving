# 0이있으면 그 전의 수는 합산에서 제외
# 나머지는 다 합산
# 입력시 0을 쓸 때에는 지울 수 있는 수가 있어야함

nums=[]

for _ in range(int(input())):
    num=int(input())
    if nums and num==0:
        nums.pop()
    else:
        nums.append(num)

print(sum(nums))
   