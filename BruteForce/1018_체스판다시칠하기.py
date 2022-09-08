# M*N의 무작위 보드를 잘라서 8*8의 체스판으로 만든다.
# 체스판은 검,흰이 번갈아가며 존재
# 체스판의 종류는 특정한 곳의 모서리 색깔에 따라 2가지로 나뉨
# 무작위 보드를 8*8으로 잘라낸 후 체스판화 해야함
# 이때 다시 칠해야하는 정사각형의 '최소' 개수 구하기


# 1.각 원소 순회하면서 8*8범위 선택
# 2.해당 범위에서 케이스1,2 비교


board=[]
coloringCounts=[]

case1=[list('BWBWBWBW'),
       list('WBWBWBWB'),
       list('BWBWBWBW'),
       list('WBWBWBWB'),
       list('BWBWBWBW'),
       list('WBWBWBWB'),
       list('BWBWBWBW'),
       list('WBWBWBWB')]

case2=[list('WBWBWBWB'),
       list('BWBWBWBW'),
       list('WBWBWBWB'),
       list('BWBWBWBW'),
       list('WBWBWBWB'),
       list('BWBWBWBW'),
       list('WBWBWBWB'),
       list('BWBWBWBW')]

N,M=map(int,input().split(' '))
for _ in range(N):
    board.append(list(input()))


for baseY in range(N-7):
    for baseX in range(M-7):
        count1=0
        count2=0
        for y in range(8):
            for x in range(8):
                if case1[y][x]!=board[baseY+y][baseX+x]:
                   count1+=1
                if case2[y][x]!=board[baseY+y][baseX+x]:
                   count2+=1
        coloringCounts.extend([count1,count2])

print(min(coloringCounts))