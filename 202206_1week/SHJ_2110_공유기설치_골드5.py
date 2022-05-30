# 2110번 공유기설치 골드5
# 문제
# 도현이의 집 N개가 수직선 위에 있다. 각각의 집의 좌표는 x1, ..., xN이고, 집 여러개가 같은 좌표를 가지는 일은 없다.
# 도현이는 언제 어디서나 와이파이를 즐기기 위해서 집에 공유기 C개를 설치하려고 한다. 최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에, 한 집에는 공유기를 하나만 설치할 수 있고, 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.
# C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 집의 개수 N (2 ≤ N ≤ 200,000)과 공유기의 개수 C (2 ≤ C ≤ N)이 하나 이상의 빈 칸을 사이에 두고 주어진다. 둘째 줄부터 N개의 줄에는 집의 좌표를 나타내는 xi (0 ≤ xi ≤ 1,000,000,000)가 한 줄에 하나씩 주어진다.

# 출력
# 첫째 줄에 가장 인접한 두 공유기 사이의 최대 거리를 출력한다.

# 예제 입력 1 
# 5 3
# 1
# 2
# 8
# 4
# 9
# 예제 출력 1 
# 3
# 힌트
# 공유기를 1, 4, 8 또는 1, 4, 9에 설치하면 가장 인접한 두 공유기 사이의 거리는 3이고, 이 거리보다 크게 공유기를 3개 설치할 수 없다.

import sys

def checkDistance(n:int, c:int, x:list, s:int, e:int, mid:int):
    cnt = 1  # 설치한 공유기 개수 첫 위치 1개로 시작
    i = 0    
    while i < len(x)-1:
        bFind = False   # for문처럼 i++를 해주기 위해 필요한 bool 변수
        for ii in range(i+1, len(x)):
            if x[ii] - x[i] >= mid:     # 두 집 사이의 거리가 mid 보다 크거나 같으면 공유기 설치, 아니면 ii++
                cnt += 1                
                bFind = True
                if c == cnt:     # 공유기를 다 설치했으면 종료, mid 조정
                    s = mid+1
                    return s, e, True
                
                break            # 아직 부족하면 i 높여서 루프 진행

            if n - ii < c -cnt:  # 남은 집 보다 남은 공유기가 더 많으면 mid를 조정
                e = mid-1
                return s,e, False
           
        if bFind == False:  # 발견하지 못했으면 i+1, 발견 했으면 i=ii
            i += 1
        else:
            i = ii

    e = mid - 1             # 끝까지 발견하지 못한 경우 mid를 줄인다
    return s, e, False



n, c =map(int,sys.stdin.readline().split())    # 집의 개수, 공유기의 개수

x = []                                      
for _ in range(n):
    x.append(int(sys.stdin.readline()))        # 집의 위치

x.sort()           # 집의 위치 정렬

s = 1
e = x[n-1]-x[0]    # 가능한 최대 거리는 첫번째집 - 마지막집 

# 이분탐색 시작
while s <= e:
    mid = (s+e)//2
    s, e, bResult = checkDistance(n,c,x,s,e,mid)
    if bResult == True:  # 조건을 만족을 때의 mid 값을 저장
        answer = mid
print(answer)