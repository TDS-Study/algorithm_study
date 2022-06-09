"""문제
명절이 되면, 홍익이 집에는 조카들이 놀러 온다. 떼를 쓰는 조카들을 달래기 위해 홍익이는 막대 과자를 하나씩 나눠준다.

조카들이 과자를 먹는 동안은 떼를 쓰지 않기 때문에, 홍익이는 조카들에게 최대한 긴 과자를 나눠주려고 한다.

그런데 나눠준 과자의 길이가 하나라도 다르면 조카끼리 싸움이 일어난다. 따라서 반드시 모든 조카에게 같은 길이의 막대 과자를 나눠주어야 한다.

M명의 조카가 있고 N개의 과자가 있을 때, 조카 1명에게 줄 수 있는 막대 과자의 최대 길이를 구하라.

단, 막대 과자는 길이와 상관없이 여러 조각으로 나눠질 수 있지만, 과자를 하나로 합칠 수는 없다. 단, 막대 과자의 길이는 양의 정수여야 한다.

입력
첫째 줄에 조카의 수 M (1 ≤ M ≤ 1,000,000), 과자의 수 N (1 ≤ N ≤ 1,000,000)이 주어진다.

둘째 줄에 과자 N개의 길이 L1, L2, ..., LN이 공백으로 구분되어 주어진다. 과자의 길이는 (1 ≤ L1, L2, ..., LN ≤ 1,000,000,000) 를 만족한다.

출력
첫째 줄에 조카 1명에게 줄 수 있는 막대 과자의 최대 길이를 출력한다.

단, 모든 조카에게 같은 길이의 막대과자를 나눠줄 수 없다면, 0을 출력한다.

https://www.acmicpc.net/problem/16401

3 10
1 2 3 4 5 6 7 8 9 10

8
"""

import sys


nOfNiblings, nOfCandies = map(int, input().split())
candies = list(map(int, sys.stdin.readline().split()))
candies.sort()

def check(mid: int) -> bool:
    result = False
    cnt = 0;

    for i in candies:
        cnt += i // mid

        if cnt >= nOfNiblings:
            result = True
            break
    
    return result

begin, end = 1, max(candies)
mid = 0
maxValue = 0

while(begin <= end):
    mid = (begin + end) // 2

    if(check(mid)):
        begin = mid + 1
        maxValue = mid
    else:
        end = mid - 1

print(maxValue)