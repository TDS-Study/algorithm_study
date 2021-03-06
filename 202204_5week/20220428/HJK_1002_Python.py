# 문제 
# 조규현과 백승환은 터렛에 근무하는 직원이다. 하지만 워낙 존재감이 없어서 인구수는 차지하지 않는다. 다음은 조규현과 백승환의 사진이다.
# 이석원은 조규현과 백승환에게 상대편 마린(류재명)의 위치를 계산하라는 명령을 내렸다. 조규현과 백승환은 각각 자신의 터렛 위치에서 현재 적까지의 거리를 계산했다.
# 조규현의 좌표 (x1, y1)와 백승환의 좌표 (x2, y2)가 주어지고, 조규현이 계산한 류재명과의 거리 r1과 백승환이 계산한 류재명과의 거리 r2가 주어졌을 때, 류재명이 있을 수 있는 좌표의 수를 출력하는 프로그램을 작성하시오.

# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
n = int(input())
# 각 테스트 케이스는 다음과 같이 이루어져 있다.
# 한 줄에 x1, y1, r1, x2, y2, r2가 주어진다. x1, y1, x2, y2는 -10,000보다 크거나 같고, 10,000보다 작거나 같은 정수이고, r1, r2는 10,000보다 작거나 같은 자연수이다.
result = []

for i in range(n):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())

    # 두 점 사이의 거리 d = ((x2-x1)제곱+(y2-y1)제곱) 제곱근
    d = (((x2-x1)**2) + ((y2-y1)**2)) ** 0.5

    # 두 원이 만나는 점의 갯수 x
    x = 0

    if d == 0:
        # 동심원
        if r1 == r2:
            # 두 원 반지름 일치 의 경우 무한대
            x = -1
        else:
            # 안만남
            x = 0
    else:
        if d == (r1 + r2):
            # 두 원이 외부에서 1점에서 만나는 경우
            x = 1
        elif d == abs(r2-r1):
            # 큰원 안에 작은 원이 1점에서 만나는 경우
            x = 1
        elif abs(r1-r2) > d:
            # 큰원 안에 작은원이 있고 안만나는 경우
            x = 0        
        elif d > (r1 + r2):
            # 두 원이 멀리 떨어진 경우
            x = 0
        else:
            # 나머지의 경우 2점에서 만남
            x = 2
    
    result.append(x)        

for j in result:
    print(j)
