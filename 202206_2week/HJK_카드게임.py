"""

n 라운드 마다 2명의 플레이어가 카드 5개 씩 받는다
셔플이 잘 되지 않은 라운드 수를 출력

1. 각 라운드에 두 명이 받은 10장의 카드에 중복이 있으면 셔플 실패
2. 각 플레이어의 카드 중 2장이 직전 라운드와 같다면 셔플 실패

"""

import random

iRound = int
cards1, cards2 = [], []

def getInput():
    global iRound, cards1, cards2

    # 라운드(1~100)를 랜덤하게 생성 
    iRound = random.randint(1, 3)

    for i in range(iRound):
        # 1~52 까지 숫자를 랜덤하게 5개 뽑고 라운드수 만큼 추가
        a = [random.randrange(1,52,1) for j in range(5)]
        # 검증하기 쉽도록 정렬해준다
        a.sort()
        cards1.append(a)

        b = [random.randrange(1,52,1) for j in range(5)]
        b.sort()
        cards2.append(b)
    
    print(cards1, '\n', cards2)

# 입력을 받는다
getInput()

def rule1(card1 = [], card2 = []):
    # 두 덱의 유일한 숫자가 10개이면 통과
    uniqueCount = len(set(card1 + card2))
    print(f"Check1 Unique Count: {uniqueCount}")

    if uniqueCount == 10:
        return True
    else:        
        return False

def rule2(prevCards = [], cards = []):
    # 두 덱의 
    if len(prevCards) == 0:
        print("no prev cards")
        return True
    else:
        uniqueCount = len(set(prevCards + cards))
        print(f"Check2 Unique Count: {uniqueCount}")

        if uniqueCount > 8:
            return True
        else:
            return False

prevRound1, prevRound2 = [], []
failCnt = 0

# 라운드 별로 체크한다
for i in range(iRound):

    if rule1(cards1[i], cards2[i]) and \
        rule2(cards1[i], prevRound1) and \
        rule2(cards2[i], prevRound2):
        pass
    else:
        failCnt += 1
    
    prevRound1 = cards1[i]
    prevRound2 = cards2[i]

print(failCnt)
    

