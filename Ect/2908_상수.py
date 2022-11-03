A,B=input().split() #문자형으로  A,B  받기

a=''
b=''
# 문자형 변수 a,b 선언

for i in A[::-1]: # 리스트 슬라이싱 사용
                  # a:b:c 에서 a~b는 범위를 의미하고 c는 간격을 의미함
    a=a+i

for i in B[::-1]:
    b=b+i

#문자를 역으로 순회하며 하나씩 더해 역순 문자열 만들기


if int(a)>int(b): #정수형으로 변환하여 비교 
   print(a)
else:
   print(b)
