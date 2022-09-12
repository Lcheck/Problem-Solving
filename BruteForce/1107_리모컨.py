# 0~9
# +:현재채널+1
# -:현재채널-1

# 채널은 무한대, 0에서 -하면 채널 안변함

# 이동하려는 채널N
# 특정 버튼 사용X

# N으로 이동하기 위해 눌러야 하는 버튼의 최소 수
# 현재 채널은 100



N=int(input())
channer=list(map(int,list(str(N))))#이동 하려는 채널
M=int(input())#고장난 버튼의 개수
pushCount=0#버튼 누른 횟수
buttonList=[i for i in range(10)]#기존 버튼 리스트
preChannels=[] #후보 채널
absList=[] #절대값리스트

if N>=100: #<<<<1. +,-만 이용하는 경우>>>> 고장난 버튼이 10개인경우, 
   result2=N-100 
else:
   result2=100-N


if M!=0:
  breakButtons=list(map(int,input().split(' ')))#고장난 버튼들

  if M==10: #버튼이 다 고장난 경우
     print(result2)
     exit()

  for i in breakButtons:   
     buttonList.remove(i)
else:                                # <<<<2.숫자 버튼만 이용하는 경우 (고장난 버튼이 없는 경우)>>>>
    print(min(len(channer),result2))
    exit()


# <<<<3.숫자 버튼 이용하고, +,-를 이용하는 경우>>>>

# 0부터 해당 수*2 까지 카운트 하면서 가진 버튼으로 나열 할 수 있는 모든 경우의 수를 리스트에 넣는다.
# 리스트의 수중 목표 채널과 절대값이 제일 작은 수를 고른다

for num in range((N+10)*2): #숫자카운트 -> N의 크기를 작게할경우 예외가 발생
    flag=True
    for i in list(str(num)): #해당 숫자 각 자릿수의 수 순회
        if int(i) in breakButtons: #만일 해당 숫자의 자릿수 수가 부서진 버튼들에 존재하는 수면
            flag=False
            break #탈출
    if(flag):
       preChannels.append(num)

for c in preChannels:
    absList.append(abs(N-c)) #절대값 구하기

minAbs=min(absList)
cIdx=absList.index(minAbs) #제일 작은 절대값의 인덱스 = 채널 후보 중 선택된 채널의 인덱스
nowChannel=preChannels[cIdx]
result=minAbs+len(str(nowChannel)) 
print(min(result,result2))
   


#FAIL

# #각 자리수에 해당되는 버튼은 목표 값과 가장 가까운 값으로 구성

# maxValue=0
# maxValueIdx=0
# nowChanner=[]
# flag=False
# for i in range(len(channer)):
#     for idx,ele in enumerate(buttonList):
#         if channer[i]==0:  #해당자리가0인경우 가장 현재 버튼 중 가장 큰 수 저장
#            nowChanner.append(max(buttonList))
#            print(nowChanner)
#            pushCount+=1
#            flag=True
#            break
#     if flag:
#        flag=False
#        continue

#        if ele>=channer[i]: #숫자가 커지거나 같아진 순간 해당 값과 인덱스 저장
#            maxValue=ele
#            maxValueIdx=idx
#            break

#     if (pow(channer[i]-buttonList[maxValueIdx-1],2))<(pow(maxValue-channer[i],2)): #첫째 자리보다 한단계 큰수와 한단계 작은수의 절대값비교/작은수가 절대값 작은경우
#         nowChanner.append(buttonList[maxValueIdx-1]) #해당 수를 첫째자리로
#     else: #아니거나 같으면
#         nowChanner.append(maxValue)#큰 수를 첫째자리로
        
#         pushCount+=1

# nowChannerNum=int(''.join(map(str,nowChanner)))   #현재채널을 숫자로 변환
# channerNum=int(''.join(map(str,channer)))   #이동하려는채널을 숫자로 변환


# while nowChannerNum!=channerNum: ##두숫자가 같아질때까지
#       if nowChannerNum<channerNum: #지금 작은 경우
#          nowChannerNum+=1
         
#       else: #큰경우
#         nowChannerNum-=1
#       pushCount+=1
# print(nowChanner)
# print(min(pushCount,pushCount2))
