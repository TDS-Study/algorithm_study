'''
2468_안전영역_실버1
'''

from collections import deque

class Zone:
    x = int()
    y = int()
    al = int()
    def __init__(self, al, x, y):
        self.al = al
        self.x = x
        self.y = y

def bfs(x, y, n, h, visit):
    existSafetyZone = False
    
    queue = deque([Zone(altitude[x][y], x, y)])
    # 방문 했음
    
    while queue:
        cur =  queue.popleft()
        visit[cur.x][cur.y] = True
        # 세이프티 존 있음
        if cur.al > h:
            existSafetyZone = True
        
            # 상
            if cur.y-1 >= 0 and visit[cur.x][cur.y-1] == False:
                queue.append(Zone(altitude[cur.x][cur.y-1], cur.x, cur.y-1))
                # visit[cur.x][cur.y-1] = True
            # 하
            if cur.y+1 < n and visit[cur.x][cur.y+1] == False:
                queue.append(Zone(altitude[cur.x][cur.y+1], cur.x, cur.y+1))
                # altitude[cur.x][cur.y+1] = True
            # 좌
            if cur.x-1 >= 0 and visit[cur.x-1][cur.y] == False:
                queue.append(Zone(altitude[cur.x-1][cur.y], cur.x-1, cur.y))
                # altitude[cur.x-1][cur.y] = True
            # 우
            if cur.x+1 < n and visit[cur.x+1][cur.y] == False:
                queue.append(Zone(altitude[cur.x+1][cur.y], cur.x+1, cur.y))
                # altitude[cur.x+1][cur.y] = True
        
    return existSafetyZone    # words 리스트에 target은 있으나 변환할 수 없는 경우

def countSafetyZone(n, h):
    visit = [[False for i in range(n)] for j in range(n)]
    safetyZone = 0
    for x in range(n):
        for y in range(n):
            if visit[x][y] == True:
                continue
            if altitude[x][y] <= h:
                visit[x][y] = True
                continue

            existSafetyZone = bfs( x, y,n, h, visit)
            if existSafetyZone == True:
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
min_v = 100
for i in range(n):
    row = list(map(int, input().split()))
    # row = list(map(int, sys.stdin.readline().split()))
    
    # bfs 실행할 범위 찾기
    if(max_v < max(row)):
        max_v = max(row)
    if(min_v > min(row)):
        min_v = min(row)
    altitude.append(row)

n = 5
altitude = []
altitude.append(list(map(int, '6 8 2 6 2'.split())))
altitude.append(list(map(int, '3 2 3 4 6'.split())))
altitude.append(list(map(int, '6 7 3 3 2'.split())))
altitude.append(list(map(int, '7 2 5 3 6'.split())))
altitude.append(list(map(int, '8 9 5 2 7'.split())))
min_v = 2
max_v = 9

solution(n, min_v, max_v)

