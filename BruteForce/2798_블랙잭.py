N,M=map(int,input().split())
cards=list(map(int,input().split()))

results=set() #중복제거를 위한 집합자료형
answer=0

for a in cards: #주어진 카드번호 순회
    sum=0 #3장의 합을 위한 변수 초기화
    for b in cards[cards.index(a)+1:]: #a 이후의 모든 원소들
        for c in cards[cards.index(b)+1:]: #b 이후의 모든 원소들
            sum=a+b+c 
            results.add(sum)

#n개의 수열에서 중복을 제외하고 3개를 뽑은 모든 경우의 수를 구하는 반복문


results=list(results) #정렬을 위해 집합자료형을 리스트로 변환
results.sort() #정렬

for index,value in enumerate(results): # enumerate는 인덱스와 값을 튜플형태로 반환
    if value>M: # 기준이 되는 합보다 큰 값에 도달하면
       answer=results[index-1] #이전 값이 합을 넘지 않는 최대의 값이므로 정답에 저장 후 종료
       break
    else:   # 아니라면 정답을 계속 갱신
       answer=value
       
print(answer)

# for a in cards:
#     sum=0
#     cards.pop(a)
#     for b in cards:
#         cards.pop(b)
#         for c in cards:
#             print(cards)
#             cards.pop(c)
#             sum=a+b+c
#             results.add(sum)
#     cards=temp

# results=list(results)
# results.sort()
# print(results)
# for index,value in enumerate(results):
#     print(value)
#     if value>M:
#         answer=results[index-1]
#         break
#     else:
#         answer=value

# print(answer)

