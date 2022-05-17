"""https://www.acmicpc.net/problem/1072

문제
김형택은 지금 몰래 Spider Solitaire(스파이더 카드놀이)를 하고 있다. 형택이는 이 게임을 이길 때도 있었지만, 질 때도 있었다. 누군가의 시선이 느껴진 형택이는 게임을 중단하고 코딩을 하기 시작했다. 의심을 피했다고 생각한 형택이는 다시 게임을 켰다. 그 때 형택이는 잠시 코딩을 하는 사이에 자신의 게임 실력이 눈에 띄게 향상된 것을 알았다.

이제 형택이는 앞으로의 모든 게임에서 지지 않는다. 하지만, 형택이는 게임 기록을 삭제 할 수 없기 때문에, 자신의 못하던 예전 기록이 현재 자신의 엄청난 실력을 증명하지 못한다고 생각했다.

게임 기록은 다음과 같이 생겼다.

게임 횟수 : X
이긴 게임 : Y (Z%)
Z는 형택이의 승률이고, 소수점은 버린다. 예를 들어, X=53, Y=47이라면, Z=88이다.
X와 Y가 주어졌을 때, 형택이가 게임을 최소 몇 번 더 해야 Z가 변하는지 구하는 프로그램을 작성하시오.

입력
각 줄에 정수 X와 Y가 주어진다.

출력
첫째 줄에 형택이가 게임을 최소 몇 판 더 해야하는지 출력한다. 만약 Z가 절대 변하지 않는다면 -1을 출력한다.

제한
1 ≤ X ≤ 1,000,000,000
0 ≤ Y ≤ X
"""


from decimal import Decimal
from math import ceil

# Decimal 을 사용하여 소수점 정확도 높인다
x, y = map(Decimal, input().split())

# 목표값인 승률 + 1
s = y//x*100 + 1

def bSearch(s, e, v):
    
    # start 와 end 가 같아지거나 반전되면 찾고자 하는 값이 없다
    if e >= s:
        # m:middle
        m = Decimal((e + s) // 2)
         
        # 찾는 수가 가운데 있으면 럭키~
        if l[m] == v:
            return m
        elif l[m] > v:
            # 가운데 숫자보다 찾는 수가 작은경우 왼쪽 절반을 찾는다
            return bSearch(l, s, m - 1, v)
        else:
            # 찾는 수가 가운데 숫자보다 큰 경우 오른쪽 절반을 찾는다
            return bSearch(l, m + 1, e, v) 
    else:
        # 찾는 값이 없다
        return -1

def cal(x, y, s):
    
    if y == x:
        return -1
    elif s == 99:
        return -1
    else:
        a = bSearch(1, x, s)

print(a)

# # 시뮬레이션 부분
# x = 10000

# for i in range(1,1000000):
#     x = Decimal(i)
#     for j in range(i):
#         y = Decimal(j)

#         s = int(y/x*100)
#         if s == 99:
#             dap = 99
#         elif y == x:
#             dap == 100
#         else:
#             dap = s + 1
        
#         a = cal(y, x)

#         # print(f"y:{y}, x:{x}, s:{s}, a:{a}")
        
#         dap2 = 99 if a == -1 else int(Decimal(y+a)/Decimal(x+a)*100)
        
#         if dap != dap2:
#             if a == 1 and dap2 > dap:
#                 #print(f"x:{x}, y:{y}, s:{s}, a:{a}")
#                 pass
#             else:
#                 print(f"dap:{dap}, dap2:{dap2}")
#                 print(f"x:{x}, y:{y}, s:{s}, a:{a}")
#         else:
#             dap3 = int(Decimal(y+a-1)/Decimal(x+a-1)*100)

#             if dap == dap3 and a != -1:
#                 print("!!!",f"x:{x}, y:{y}, s:{s}, a:{a}")
    
#     if int(x)%1000 == 0: print(f"x:{x}, y:{y}, s:{s}, a:{a}")
    