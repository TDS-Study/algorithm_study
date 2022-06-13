def checkRound(i:int):
    # 한 라운드에서 두 플레이어가 받은 카드 10장 중에서 중복되는 번호가 있는 경우
    if len(set(cards1[i] + cards2[i])) != 10:
        return 1

    # 한 플레이어가 직전 라운드에서 받은 카드 5장과 이번 라운드에서 받은 카드 5장을 비교했을 때, 중복되는 번호가 2개 이상 있는 경우
    if i > 0:
        if len(set(cards1[i]+cards1[i-1])) <= 8:
            return 1
        if len(set(cards2[i]+cards2[i-1])) <= 8:
            return 1

    return 0

n = int(input())
cards1= []
cards2= []
result = 0
for _ in range(n):
    cards1.append(list(map(int, input().split(','))))

for _ in range(n):
    cards2.append(list(map(int, input().split(','))))

for i in range(n):
    result += checkRound(i)
print(result)