N,X=map(int,input().split()) 
A=map(int,input().split()) 

#split을 사용해 문자열을 공백(split의 기본값)으로 구분하여 리스트로 만듬.
#map을 이용해 리스트의 원소를 int로 만들어 좌변에 대입
# ,를 사용하면 각 변수에 리스트의 원소를 대입해줄 수 있음 (리스트의 원소와 변수의 개수가 같아야함)

for i in A:
    if i<X:
        print(i,end=' ') #print 함수의 end인자에 값을 주게되면, 다음 출력시 줄바꿈이 되지 않으며
                            #출력 사이마다 end인자의 값이 들어감