# 문제
# 숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다. 두 숫자 카드에 같은 수가 적혀있는 경우는 없다.

# 셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 넷째 줄에는 상근이가 가지고 있는 숫자 카드인지 아닌지를 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다. 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다

# 출력
# 첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 가지고 있으면 1을, 아니면 0을 공백으로 구분해 출력한다.

# 예제 입력 1 
# 5
# 6 3 2 10 -10
# 8
# 10 9 -5 2 3 4 5 -10
# 예제 출력 1 
# 1 0 0 1 1 0 0 1

# 10815 숫자 카드

import bisect   # 이분 탐색
import random

# 테스트 데이터셋 생성
def create_dataset(n, m):
    nTest = []
    mTest = []
    for _ in range(n):
        nTest.append(random.randrange(-100,100))
    for _ in range(m):
        mTest.append(random.randrange(-100,100))
    return nTest, mTest

# 라이브러리 사용
def main_func(n, nList, mList):         
    result = ''                               # 결과값
    nList.sort()                              # 이분 탐색을 위해 정렬
    for _m in mList:
        pos = bisect.bisect_left(nList, _m)         # 리스트 내에서 _m 값이 들어갈 index 반환, 같은 값이면 왼쪽 index 반환
        if len(nList) == pos or nList[pos] != _m:   # index가 배열을 초과할 경우: 상근이가 가지고 있는 숫자 카드보다 큰 값                  
            result = result + " 0"                  # 해당 위치의 값과 다른 경우: 존재하지 않음.
        else:
            result = result + " 1"
    
    result = result[1:]  # 첫 공백 제거
    print(result)

def binary_search(arr, value):
    first, last = 0, len(arr)-1     # mid = last로 가는 경우도 있으니 last는 길이-1로 설정
    while first <= last:
        mid = (first + last) // 2
        if arr[mid] == value:
            # return mid
            return " 1"
        if arr[mid] > value:        # 왼쪽 범위 탐색 (작은 값)
            last = mid - 1
        else:                       # 오른쪽 범위 탐색 (큰 값)
            first = mid + 1
    return " 0"
    
def main(n, nList, mList):
    result = ""
    nList.sort()

    for _m in mList:
        result = result + binary_search(nList, _m)

    result = result[1:]
    print(result)


if __name__ == "__main__":
    n = int(input())                          # n: 상근이가 가지고 있는 숫자 카드의 개수 (1 <= N <= 500,000)
    nList = list(map(int, input().split()))   # nList: 상근이가 가지고 있는 숫자 카드
    m = int(input())                          # m: 상근이가 가지고 있는 숫자 카드의 개수 (1 <= M <= 500,000)
    mList = list(map(int, input().split()))   # mList: 상근이가 가지고 있는 숫자 카드
    
    # n = 50
    # m = 100
    # nList, mList = create_dataset(n,m)
    # main_func(n, nList, mList)            # 라이브러리 사용       
    main(n, nList, mList)                   # 함수