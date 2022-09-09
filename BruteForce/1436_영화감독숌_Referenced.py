#6이 세번이상 연속되는 수를 오름차순으로 정렬해야함

#1~10000까지 가다가 666이 연속되는 수면 리스트에 넣기


import re

count=1
EndNumList=[0]

N=int(input())

while len(EndNumList)<=N:
   #종말의 수 리스트가 N개가 될 때 까지
    count+=1
    EndNum=re.search('6{3}',str(count))
    if EndNum!=None:
       #종말의 수라면
       EndNumList.append(count)

print(EndNumList[N])
