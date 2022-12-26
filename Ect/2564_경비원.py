
blockWidth,blockHeight=map(int,input().split())
shopCount=int(input())
shopLocations=[]
for _ in range(shopCount+1):
    shopLocations.append(tuple(map(int,input().split())))
dongGeunLocation=shopLocations.pop()
dongGeunDirection=dongGeunLocation[0]
result=[]
#1 북 왼쪽
#2 남 왼쪽
#3 서 위쪽
#4 동 위쪽

#상점, 동근 위치는 꼭짓점 불가

def one(shopLocation):
    return abs(dongGeunLocation[1]-shopLocation[1])

def two(shopLocation):
    return min((blockHeight+dongGeunLocation[1]+shopLocation[1])
    ,(blockHeight+temp(shopLocation)))

def three(shopLocation):
    return dongGeunLocation[1]+shopLocation[1]

def temp(shopLocation):
    return (2*blockWidth)-dongGeunLocation[1]-shopLocation[1]

def four(shopLocation):
    return blockWidth+dongGeunLocation[1]-shopLocation[1]

def five(shopLocation):
    return blockHeight+shopLocation[1]-dongGeunLocation[1]

def six(shopLoaction):
    return temp(shopLoaction)-blockWidth+blockHeight

def seven(shopLocation):
    return min((blockWidth+dongGeunLocation[1]+shopLocation[1])
    ,(blockWidth+temp(shopLocation)+(4*blockHeight)))

def compareDirection(one,two):
    global shopLocation,dongGeunDirection
    return shopLocation[0]==one and dongGeunDirection==two 

for shopLocation in shopLocations:

    if shopLocation[0]==dongGeunDirection and shopLocation[1]==dongGeunLocation[1]:
        continue
    if shopLocation[0]==dongGeunDirection:
            result.append(one(shopLocation)) # 22
        
    if compareDirection(1,2) or compareDirection(2,1): ## 12
            result.append(two(shopLocation))
    if compareDirection(1,3) or compareDirection(3,1):
            result.append(three(shopLocation))
    if compareDirection(1,4):
            result.append(four(shopLocation))
    if compareDirection(4,1):
            result.append(four(shopLocation)-(2*dongGeunLocation[1])+(2*shopLocation[1]))
    if compareDirection(2,3): ## 32
            result.append(five(shopLocation))
    if compareDirection(3,2):
            result.append(five(shopLocation)+(2*dongGeunLocation[1])-(2*shopLocation[1]))
    if compareDirection(2,4) or compareDirection(4,2):
            result.append(six(shopLocation))
    if compareDirection(3,4) or compareDirection(4,3):
            result.append(seven(shopLocation))

print(sum(result))

#  1 1 절대값차이 1
#  2 2 절대값차이 1
#  3 3 절대값차이 1
#  4 4 절대값차이 1
#  1 2 min(높이+동근좌표+상점좌표 , 높이+넓이-동근좌표+넓이-상점좌표) 2
#  2 1 min(높이+동근좌표+상점좌표 , 높이+넓이-동근좌표+넓이-상점좌표) 2
#  1 3 동근좌표+상점좌표 3
#  3 1 동근좌표+상점좌표 3
#  1 4 넓이-상점좌표 + 동근좌표 4
#  4 1 넓이-동근좌표 + 상점좌표 4-2
#  2 3 상점좌표+높이-동근좌표 5
#  3 2 동근좌표+높이-상점좌표 5-2
#  2 4 넓이-동근좌표+높이-상점좌표 6
#  4 2 넓이-동근좌표+높이-상점좌표 6
#  3 4 min(넓이+동근좌표+상점좌표 , 넓이+높이-동근좌표+높이-상점좌표) 7
#  4 3 min(넓이+동근좌표+상점좌표 , 넓이+높이-동근좌표+높이-상점좌표) 7


