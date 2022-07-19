'''
2468_안전영역_실버1
'''

from collections import deque

def bfs(x, y, n, h, visit):
    queue = deque([(x, y)])
    while queue:
        x, y =  queue.popleft()
        # 상
        if y-1 >= 0 and not visit[x][y-1] and altitude[x][y-1] > h:
            queue.append((x, y-1))
            visit[x][y-1] = True
        # 하
        if y+1 < n and not visit[x][y+1] and altitude[x][y+1] > h:
            queue.append((x, y+1))
            visit[x][y+1] = True
        # 좌
        if x-1 >= 0 and not visit[x-1][y] and altitude[x-1][y] > h:
            queue.append((x-1,y))
            visit[x-1][y] = True
        # 우
        if x+1 < n and not visit[x+1][y] and altitude[x+1][y] > h:
            queue.append((x+1, y))
            visit[x+1][y] = True
        

def countSafetyZone(n, h):
    visit = [[False for i in range(n)] for j in range(n)]
    safetyZone = 0
    for x in range(n):
        for y in range(n):
            if visit[x][y] == True: # 방문 했으면 패스
                continue
            if altitude[x][y] <= h: # 물에 잠기는 지역이면 패스
                visit[x][y] = True
                continue
            
            visit[x][y] = True
            bfs( x, y,n, h, visit)  # 안전지역 1건 확인하고 옴.
            safetyZone += 1
    return safetyZone

def solution(n, min, max):
    answer = 0
    
    for h in range(min,max+1):
        safetyZone = countSafetyZone(n, h)
        if answer < safetyZone:
            answer = safetyZone
    print(answer)

n = int(input())
altitude = []
max_v = 1
min_v = 0   # 비가 오지 않는 경우 고려?
for i in range(n):
    row = list(map(int, input().split()))
    
    # bfs 실행할 범위 찾기
    if(max_v < max(row)):
        max_v = max(row)
    altitude.append(row)

# n = 5
# altitude = []
# altitude.append(list(map(int, '6 8 2 6 99'.split())))
# altitude.append(list(map(int, '3 2 3 4 6'.split())))
# altitude.append(list(map(int, '6 7 3 3 2'.split())))
# altitude.append(list(map(int, '7 2 5 3 6'.split())))
# altitude.append(list(map(int, '8 9 5 2 7'.split())))
# min_v = 2
# max_v = 9

solution(n, min_v, max_v)

