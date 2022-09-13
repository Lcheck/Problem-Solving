# 튜플로 이뤄진 수열이 있다.
# 각 튜플의 첫원소는 숫자 둘째원소는 색상값이다.
# 같은 색상 값을 골라 교체할 수 있다.
# 이것을 반복 했을 때 튜플의 첫 원소의 값이 오름차순으로 정렬 될 수 있는가?


# 어차피 같은 색상을 바꿔도 전체 색상 조합에는 변화가 없다.
#어차피 Y가 출력될 인풋은 숫자값을 기준으로 정렬해도 색상 순서가 바뀌지 않는다
#그냥 숫자 값 기준으로 정렬 후
#색상값에 손상이 있는 경우만 N처리 해주면 된다.

N,K=map(int,input().split(' '))
blocks=[]

for i in range(N):
   blocks.append(list(map(int,input().split(' '))))

compareBlocks=blocks[:]
blocks=sorted(blocks,key= lambda x : x[0])

for i in range(N):
    if blocks[i][1]!=compareBlocks[i][1]:
       print('N')
       exit()

print('Y')


# ----Fail Code
# 같은 색상별로 숫자들을 모은다.
# 모은 숫자들을 정렬한다.
# 다시 원래 색상 자리에 놓는다.
# 정렬 됐는지 확인한다.
# O(N^2)-->시간초과

# N,K=map(int,input().split(' '))
# blocks=[]
# compareBlockNums=[]
# colorByBlockNums=[[] for _ in range(K+1)]

# for i in range(N):
#    blocks.append(list(map(int,input().split(' '))))
#    compareBlockNums.append(blocks[i][0])

# for block in blocks:   #같은 색상별로 숫자들을 모은다.
#     for color in range(1,K+1):
#         if block[1]==color:
#            colorByBlockNums[color].append(block[0])
#            break

# for i in colorByBlockNums: #모은 숫자들을 정렬한다.
#     i.sort(reverse=True)

# for i in blocks:   #다시 원래 색상 자리에 놓는다.
#     for idx in range(1,K+1):
#         if i[1]==idx:
#            i[0]=colorByBlockNums[idx].pop()

# compareBlockNums.sort()

# for idx,i in enumerate(compareBlockNums):
#     if blocks[idx][0]!=i:
#        print('N')
#        exit()
# print('Y')
