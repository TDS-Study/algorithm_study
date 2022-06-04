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
    iRound = random.randint(1, 100)

    for i in range(iRound):
        # 1~52 까지 숫자를 랜덤하게 5개 뽑고 라운드수 만큼 추가
        cards1.append([random.randrange(1,52,1) for j in range(5)])
        cards2.append([random.randrange(1,52,1) for j in range(5)])

# 입력을 받는다
getInput()

prevRound 

# 라운드 별로 체크한다
for i in range(iRound):
    

