

from re import I


n, c = map(int,input().split())                 # nephew 조카, cookie
l = list(map(int, input().split())) # length

l.sort(reverse=True)    # 내림차순 정렬
s = 1
e = max(l)

def isOk(mid:int):
    cnt = 0 # mid로 가능한 과자의 개수
    for length in l:
        i =1
        if length < mid:
            continue
        else:
            while length >= mid*i:
                cnt += 1
                i += 1
        
        if cnt >= n:
            return True
    
    if cnt < n:
        return False
    else:
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