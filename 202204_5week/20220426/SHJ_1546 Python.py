# 1546번 평균

n=int(input())                 # 과목 개수 받아서 int 변환
iScore =list(map(int, input().split()))           # 점수 나열된 string 받음

total_new_score = 0            # 변환된 점수 총 합
max_score = max(iScore)                  # 최고 점수

# 변환 된 점수 합계
for i in range(n):
    total_new_score += round(iScore[i]/max_score * 100)

avg_new_score = round(total_new_score / n,5)

print(avg_new_score)
