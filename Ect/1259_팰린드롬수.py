# 팰린드롬수 만들기
# 각 줄 별로 팰린드롬수 구별 후 yes or no 출력

#반복문으로 첫번째 자리와 마지막 자리를 한칸씩 좁혀가며 비교한다.
#다른 게 있을 경우 no 출력, 반복문을 다 돌아도 다른 게 없으면 yes 출력
# // 연산으로 인해 홀, 짝 구분 안해도됨

flag=True

while(1):

    inputNumLine=input();
    if(inputNumLine=='0'):
       break

    numLine=list(map(int,inputNumLine))
    length=len(numLine)
    
    for n in range(length//2):
        if numLine[n]!=numLine[length-n-1]:
           print('no')
           flag=False
           break

    if(flag): 
       print('yes')
    flag=True    