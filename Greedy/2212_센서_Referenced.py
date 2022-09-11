# 고속도로 위에 N개의 센서를 설치했음
# 센서들이 자료를 저장할 집중국은 최대 K개 세울 수 있음
# 각 집중국은 수신 가능 영역 조절 가능
# N개의 센서는 적어도 하나의 집중국와 통신할 수 있어야함
# 각 집중국의 수신 가능 영역 거리 합의 최소를 구하라
#!단 집중국의 수신 가능 거리는 0이다. 즉 하나의 센서만 전담할 수 있다.
#-> 문장 하나하나를 꼼꼼히 읽어서 단서화하자


#idea N개의 센서에 K개의 집중국이 존재하고
#집중국 사이의 공간은 K-1개가 존재한다.
#각 집중국의 거리의 합을 가장 크게 만들어 주면된다. // 집중국의 거리는 최대범위를 기준으로 한다.
#거리가 좁을 수록 수신범위가 비효율적으로 증가하기 때문이다.

#각 집중국의 거리는 센서 사이의 거리이므로
#센서 사이의 거리를 목록화 한 뒤 큰 순서대로 K-1개 제외하면 
#나머지 거리의 합이 집중국 거리의 최소합이다.



N=int(input())
K=int(input())
sensorRanges=[]
sensors=list(map(int,input().split(' ')))
sensors.sort()

if N<K: #센서의 수보다 집중국의 수가 더 많은 경우
   print(0)
   exit()

for i in range(N-1):
    sensorRanges.append(sensors[i+1]-sensors[i])
sensorRanges.sort(reverse=True)
sensorRangesTotal=sum(sensorRanges)

for i in range(K-1):
    sensorRangesTotal-=sensorRanges[i]
print(sensorRangesTotal)
