"""문제
도현이의 집 N개가 수직선 위에 있다. 각각의 집의 좌표는 x1, ..., xN이고, 집 여러개가 같은 좌표를 가지는 일은 없다.

도현이는 언제 어디서나 와이파이를 즐기기 위해서 집에 공유기 C개를 설치하려고 한다. 최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에, 한 집에는 공유기를 하나만 설치할 수 있고, 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.

C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오.

입력
첫째 줄에 집의 개수 N (2 ≤ N ≤ 200,000)과 공유기의 개수 C (2 ≤ C ≤ N)이 하나 이상의 빈 칸을 사이에 두고 주어진다. 둘째 줄부터 N개의 줄에는 집의 좌표를 나타내는 xi (0 ≤ xi ≤ 1,000,000,000)가 한 줄에 하나씩 주어진다.

출력
첫째 줄에 가장 인접한 두 공유기 사이의 최대 거리를 출력한다."""

#https://www.acmicpc.net/problem/2110

# 문제를 먼저 시각화 한다
# 주어진 갯수의 공유기를 가장 멀리 배치하는 방법
# 다시말해 공유기 사이의 최소 거리가 가장 먼(최대) 배치방법 구하기
# 공유기 설치 가능위치 = 집의 좌표
# 집사이의 거리를 미리 구할 수 있음
# 공유기의 최대 거리는 가장 첫 집 - 가장 끝집이다
# -> 탐색 해야 할 최대 값(거리)은 가장 큰 값은 끝집-첫집
# -> 가장 작은 거리는 각 집간 거리 중 최소값
# 공유기가 2개만 있다고 가정하면 가장 첫집, 끝집에 놓으면 최대거리

nHouse, nWifi = map(int, input().split())
lHouse = []

for i in range(nHouse):
    lHouse.append(int(input()))

def check(m, lHouse, nWifi):
    # 첫번째 집 위치
    prevLoc = lHouse[0]
    nW = nWifi - 1 # 첫번째 것  제외
    
    # 집 위치사이의 거리가 m 보다 크면 통과
    for i in lHouse:
        if (i - prevLoc) >= m:
            nW -= 1
            prevLoc = i            
        
        if nW == 0:
            # 모든 공유기를 m 이상 거리를 두고 놓았다면 패스
            return True
    
    return False

def main(nHouse = int, nWifi = int, lHouse = []):
    answer = 1

    # 집 위치로 정렬한다
    lHouse.sort()

    # 편의상 최소 집사이 거리는 1로 생각한다
    begin = 1
    # 끝집 - 첫집 거리만큼 이 최대거리이다 (공유기 2개만 놓을경우 최대거리)
    end = lHouse[len(lHouse)-1] - lHouse[0]
    # 최소 거리1 부터 최대거리 까지 가능한지 아닌지 체크해 나간다
    
    # 가능한거리가 100억이므로 2분탐색을 사용하여 탐색을 줄인다
    while(begin <= end):        
        m = (begin + end)//2

        if check(m, lHouse, nWifi) == False:        
            # m 거리로 공유기를 놓지 못했다면 m 보다 작은수 절만을 검색한다
            end = m - 1
        else:
            # m 거리로 공유기를 전부 놓을 수 있다면 더 큰 거리 절반을 검색한다            
            begin = m + 1
            # 공유기를 놓을 수 있었던 m은 기억해둔다. (이후 조건이 만족하지 않은 채 탐색이 끝날 수도 있음)
            answer = m
    
    return answer

a = main(nHouse, nWifi, lHouse)

print(a)
