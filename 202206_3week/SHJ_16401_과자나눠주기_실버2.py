n, c = map(int,input().split())                 # nephew 조카, cookie
l = list(map(int, input().split())) # length

l.sort(reverse=True)    # 내림차순 정렬
s = 1
e = max(l)

def isOk(mid:int):
    cnt = 0 # mid로 가능한 과자의 개수
    for length in l:
        l_cnt = length // mid
        if l_cnt < 1:    # 내림차순 정렬을 했기 때문에 length가 mid보다 작기 시작하면 나머지 요소는 다 작다고 봐야함.
            break
        else:
            cnt += l_cnt # mid 기준 몇개로 나눌 수 있는지 판단.
    
        if cnt >= n:     # 과자 개수가 조카 인원수를 충족하면 for문을 멈추고 True 리턴
            return True
    
    if cnt < n:         # 과자 개수가 부족하면 False
        return False
    else:               # 과자 개수가 충분하면 True
        return True

if sum(l) < n:      # 모든 과자를 합쳐도 조카 수 보다 작은 경우
    print(0)
else:
    while s <= e:
        mid = (s+e)//2

        if(isOk(mid)):
            answer = mid
            s = mid + 1
        else:
            e = mid -1
    print(answer)