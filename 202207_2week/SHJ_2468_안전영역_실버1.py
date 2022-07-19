'''
2468_안전영역_실버1
'''

from collections import deque
import sys

class Zone:
    x = int()
    y = int()
    al = int()
    def __init__(self, al, x, y):
        self.al = al
        self.x = x
        self.y = y

class Coordi:
    x = int()
    y = int()
    def __init__(self, x, y):
        self.x = x
        self.y = y

def bfs(coordi):
    safetyZones = 0
    
    while coordi:
        safetyZones += 1
        queue = deque([coordi.pop(0)])
        while queue:
            cur =  queue.popleft()
            
            # 상
            if [cur[0], cur[1]-1] in coordi:
                coordi.remove([cur[0], cur[1]-1])
                queue.append([cur[0], cur[1]-1])
            # 하
            if [cur[0], cur[1]+1] in coordi:
                coordi.remove([cur[0], cur[1]+1])
                queue.append([cur[0], cur[1]+1])
            # 좌
            if [cur[0]-1, cur[1]] in coordi:
                coordi.remove([cur[0]-1, cur[1]])
                queue.append([cur[0]-1, cur[1]])
            # 우
            if [cur[0]+1, cur[1]] in coordi:
                coordi.remove([cur[0]+1, cur[1]])
                queue.append([cur[0]+1, cur[1]])
        
    return safetyZones    # words 리스트에 target은 있으나 변환할 수 없는 경우

def countSafetyZone(n, h):
    coordi = []
    for x in range(n):
        for y in range(n):
             if altitude[y][x] > h:
                coordi.append([x,y])  # 좌표 리스트로 가야지

    safetyZones = bfs(coordi)
    return safetyZones

def solution(n, min, max):
    answer = 0
    for h in range(min,max+1):
        safetyZones = countSafetyZone(n, h)
        if answer < safetyZones:
            answer = safetyZones
    print(answer)

# n = int(input())
# altitude = []
# max_v = 1
# min_v = 100
# for i in range(n):
#     # row = list(map(int, input().split()))
#     row = list(map(int, sys.stdin.readline().split()))
    
#     # bfs 실행할 범위 찾기
#     if(max_v < max(row)):
#         max_v = max(row)
#     if(min_v > min(row)):
#         min_v = min(row)
#     altitude.append(row)

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

