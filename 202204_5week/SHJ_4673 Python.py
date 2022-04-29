# 4673번 셀프넘버
# 30840 KB
# 368 ms

def d(total, value):
    total = total + value%10
    if value /10 > 0:
        # print("total: " + str(total) + " value: " + str(value))
        total = d(total, int(value/10)) 

# 100
        
    
    return total

nList = []

# 리스트에 1~10000 할당
for i in range(1,10000):
    nList.append(i)


idx = 0
while(True):
    # idx가 nList 리스트의 개수보다 많으면 종료
    if idx >= len(nList):
        break

    # 현재 인덱스의 nList 리스트 값 할당    
    value = nList[idx]
    # print(value)
    while(True):
        # d함수 계산
        result = value + d(0, value)
        # 10000 이하, result가 nList안에 있으면 진행
        # (ex. d(n) = 110이 두번째로 나온 경우라면, 그 이후의 결과는 똑같을 것이기 때문에 Break함)
        if result <= 10000 and result in nList:
            nList.remove(result) # nList 리스트에서 result값 제외
            value = result # result값을 사용하여 d 함수 한번더 실행
        else:
            break
    
    idx = idx + 1

# print(nList)
for v in nList:
    print(v)
