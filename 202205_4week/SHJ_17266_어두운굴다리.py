# 17266번 어두운굴다리

# 문제
# 인하대학교 후문 뒤쪽에는 어두운 굴다리가 있다. 겁쟁이 상빈이는 길이 조금이라도 어둡다면 가지 않는다. 따라서 굴다리로 가면 최단거리로 집까지 갈수 있지만, 굴다리는 어둡기 때문에 빙빙 돌아서 집으로 간다. 안타깝게 여긴 인식이는 굴다리 모든 길 0~N을 밝히게 가로등을 설치해 달라고 인천광역시에 민원을 넣었다. 인천광역시에서 가로등을 설치할 개수 M과 각 가로등의 위치 x들의 결정을 끝냈다. 그리고 각 가로등은 높이만큼 주위를 비출 수 있다. 하지만 갑자기 예산이 부족해진 인천광역시는 가로등의 높이가 높을수록 가격이 비싸지기 때문에 최소한의 높이로 굴다리 모든 길 0~N을 밝히고자 한다. 최소한의 예산이 들 높이를 구하자. 단 가로등은 모두 높이가 같아야 하고, 정수이다.
# 가로등의 높이가 H라면 왼쪽으로 H, 오른쪽으로 H만큼 주위를 비춘다.

# 입력
# 첫 번째 줄에 굴다리의 길이 N 이 주어진다. (1 ≤ N ≤ 100,000)
# 두 번째 줄에 가로등의 개수 M 이 주어진다. (1 ≤ M ≤ N)
# 다음 줄에 M 개의 설치할 수 있는 가로등의 위치 x 가 주어진다. (0 ≤ x ≤ N)
# 가로등의 위치 x는 오름차순으로 입력받으며 가로등의 위치는 중복되지 않으며, 정수이다.

# 출력
# 굴다리의 길이 N을 모두 비추기 위한 가로등의 최소 높이를 출력한다.

import math
# 리스트 연산 for문 도는건 동일함
def main2(n:int, m:int, x:list):
    x2 = x.copy()   # x: 2, 4, 7
    x2.pop(0)       # x2: 4, 7
    
    d = [y-x for x, y in zip(x, x2)]
    d.append(x[0]*2)
    d.append((n - x[m-1])*2)
    return math.ceil(max(d)/2)

# while문으로 두 가로등 사이의 거리를 구함
def main(n:int, m:int, x:list):
    max = 0
    
    # 두 가로등 사이의 거리 최대값
    for i in range(1, len(x)):
        if max < x[i] - x[i-1]:
            max = x[i] - x[i-1]

    # 시작점 ~ 첫 가로등 사이의 거리
    if max < (x[0] - 0)*2:
        max = (x[0] - 0) * 2
    # 마지막 가로등 ~ 끝점 사이의 거리
    if max < (n - x[len(x)-1])*2:
        max = (n - x[len(x)-1])*2

    # 최대 거리 /2
    h = math.ceil(max/2)
    return h


if __name__ == "__main__":
    n = int(input())        # 굴다리의 길이
    m = int(input())        # 가로등의 개수
    x = list(map(int, input().split())) # 가로등 들의 위치
    
    result = main(n, m, x)
    # result = main2(n, m, x)
    print(result)