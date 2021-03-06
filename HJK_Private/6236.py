"""문제
Farmer John is an astounding accounting wizard and has realized he might run out of money to run the farm. He has already calculated and recorded the exact amount of money (1 ≤ moneyi ≤ 10,000) that he will need to spend each day over the next N (1 ≤ N ≤ 100,000) days.

FJ wants to create a budget for a sequential set of exactly M (1 ≤ M ≤ N) fiscal periods called "fajomonths". Each of these fajomonths contains a set of 1 or more consecutive days. Every day is contained in exactly one fajomonth.

FJ's goal is to arrange the fajomonths so as to minimize the expenses of the fajomonth with the highest spending and thus determine his monthly spending limit.

입력
Line 1: Two space-separated integers: N and M 
Lines 2..N+1: Line i+1 contains the number of dollars Farmer John spends on the ith day
출력
Line 1: The smallest possible monthly limit Farmer John can afford to live with.
"""

import sys

nDays, mFjs = int(), int()
nSpend = []

def getInput():
    global nDays, mFjs, nSpend    
    nDays, mFjs = map(int, input().split())
    # 배열을 미리 초기화 하여 속도 올림
    nSpend = [0 for _ in range(nDays)]

    # 입력 시 sys.stdin.readline 사용하여 속도업
    for i in range(nDays):
        nSpend[i] = int(sys.stdin.readline())

def check(middle: int) -> bool:
    global nSpend
    sum = 0
    cnt = 1

    # 날짜별 사용 금액을 middle 을 넘지 않도록 묶을 수 있는지 확인
    for i in nSpend:
        if (sum + i) <= middle:
            sum += i
        else:
            sum = i
            cnt += 1
        # 총 날짜가 기준 날짜를 넘어가면 안됨
        if cnt > mFjs:
            return False

    return True

# 입력 처리
getInput()

begin, end = max(nSpend), sum(nSpend)
middle = 0
minValue = begin

while(begin <= end):
    middle = (begin + end) // 2

    if check(middle):
        end = middle - 1
        minValue = middle
    else:
        begin = middle + 1

print(minValue)
