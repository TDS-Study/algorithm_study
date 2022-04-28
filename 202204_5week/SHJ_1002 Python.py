# 1002번 터렛
# 33768 kb
# 144 ms

from ast import Return
import math

# 두 점 사이의 거리 d
def get_d(x1, y1, x2, y2): # d = ((x1-x2)^2 + (y1-y2)^2)^(1/2)
    d = math.sqrt(math.pow(x1-x2,2) + math.pow(y1-y2,2))
    return d

# 두 원이 만나는 점의 개수
def get_point(r1, r2, d):
    point_cnt = 0
    if d == 0 and r1 == r2:                          # 두 원이 일치
        point_cnt = -1
    elif r1+r2 == d or (abs(r1-r2) == d and d != 0): # 한 점에서 만남. 외접원 or 내접원
        point_cnt = 1
    elif r1+r2 > d and abs(r1-r2) < d:               # 두 점에서 만나는 경우: r1-r2 < d < r1+r2
        point_cnt = 2                   
    elif r1+r2 < d or abs(r1-r2) > d:                # 만나지 않음. 밖으로 떨어진 원 or 안에서 떨어진 원
        point_cnt = 0
    else:
        point_cnt = 0

    return point_cnt


n = input()    # 데이터 셋 개수

for i in range(int(n)):
    x1, y1, r1, x2, y2, r2 = map(int, input().split()) # x1 y1 r1 x2 y2 r2 입력 받아서 int로 변환
    
    d = get_d(x1, y1, x2, y2)          # 두 점 사이의 거리 구하기
    cnt = get_point(r1, r2, d)         # 각 점에서 길이가 r인
    
    print(cnt)
