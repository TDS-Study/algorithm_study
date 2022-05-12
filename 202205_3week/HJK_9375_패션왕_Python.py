"""문제
해빈이는 패션에 매우 민감해서 한번 입었던 옷들의 조합을 절대 다시 입지 않는다. 예를 들어 오늘 해빈이가 안경, 코트, 상의, 신발을 입었다면, 다음날은 바지를 추가로 입거나 안경대신 렌즈를 착용하거나 해야한다. 해빈이가 가진 의상들이 주어졌을때 과연 해빈이는 알몸이 아닌 상태로 며칠동안 밖에 돌아다닐 수 있을까?

입력
첫째 줄에 테스트 케이스가 주어진다. 테스트 케이스는 최대 100이다.

각 테스트 케이스의 첫째 줄에는 해빈이가 가진 의상의 수 n(0 ≤ n ≤ 30)이 주어진다.
다음 n개에는 해빈이가 가진 의상의 이름과 의상의 종류가 공백으로 구분되어 주어진다. 같은 종류의 의상은 하나만 입을 수 있다.
모든 문자열은 1이상 20이하의 알파벳 소문자로 이루어져있으며 같은 이름을 가진 의상은 존재하지 않는다.

출력
각 테스트 케이스에 대해 해빈이가 알몸이 아닌 상태로 의상을 입을 수 있는 경우를 출력하시오."""
# https://www.acmicpc.net/problem/9375

# 테스트 케이스 갯수
t = int(input())
# 결과 저장
r = []

while(t != 0):
    # 옷의 수
    n = int(input())
    # 옷의 부위를 키, 이름들(리스트)을 값으로 가지는 딕셔너리 구성
    # { "face":["mask", "sunglasses"] }
    dict = {}

    for i in range(n):
        name, category = input().split()
        
        # 부위가 없으면 추가해준다
        if category not in dict.keys():
            dict[category] = [name]
        # 부위가 있으면 이름만 추가한다
        else:
            dict[category].append(name)
    
    # 각 부위별 갯수에 안입을경우의 수 1을 더해 옷 종류별로 곱한다
    x = 1
    for k, v in dict.items():
        x *= (len(v) + 1)

    # 알몸인 경우의수 1을 뺀다
    x = x - 1
    r.append(x)    
    
    t -= 1

print(*r, sep='\n')
