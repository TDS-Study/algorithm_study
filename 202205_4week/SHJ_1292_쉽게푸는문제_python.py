# 1292번 쉽게 푸는 문제
# 수열을 어디까지 생성할지 판단
# 1+2+3+... n => n(n+1)/2
# n(n+1)/2 > B
# n^2 + n - 2B > 0
# 근의 공식: 두 값은 음수, 양수 나옴. 큰 숫자를 사용

import math
a, b = map(int, input().split())

x1 = (-1 +math.sqrt(1-4*(-2*b))) /2 # 근의 공식
x2 = (-1 -math.sqrt(1-4*(-2*b))) /2 # 근의 공식

x = 0                               # 양수 판단
if x1>x2:
    x = math.ceil(x1)
else :
    x = math.ceil(x2)

seq = []                            # 배열 생성
for i in range(1, x+1):
    seq = seq + [i]*i

print(sum(seq[(a-1):(b)]))          # a, b 범위의 합
