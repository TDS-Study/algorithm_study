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

# Decimal 을 사용하여 소수점 정확도 높인다
x, y = map(Decimal, input().split())

def bSearch(start, end, minValue):
    global y, x, target
    # start 와 end 가 같아지거나 반전되면 끝까지 찾아본 것
    if end >= start:
        
        middle = Decimal((start + end) // 2)        
        answer = (100 * (y + middle)) // (x + middle)
                
        # 왼쪽을(작은수) 더 찾는다
        if target <= answer:
            return bSearch(start, middle - 1, middle)
        else:
            # 더 오룬쪽(큰수)를 찾는다
            return bSearch(middle + 1, end, minValue)
    else:
        # 끝까지 찾아본 후 최소값 출력
        return minValue

# # 목표값인 승률 + 1, t:target
target = ((100 * y) // x) + 1
# #print(t)
a = bSearch(x, y, target)

if y == x or target == 100:
    print(-1)
else:
    print(bSearch(1, x, x))
