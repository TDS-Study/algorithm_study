# 1546번 평균
# 메모리 30840	KB
# 시간 68 ms

# 새로운 점수로 변환: 현재 점수 / 최고점수 * 100 반환
def new_score(max_socre, cur_score): 
    return round(cur_score/max_score*100) # round를 쓰면 숫자의 자리수가 줄어들어서 더 빠른가봄.

n=int(input())                 # 과목 개수 받아서 int 변환
input_score = input()          # 점수 나열된 string 받음

score = input_score.split(' ') # 점수 나열을 ' ' 기준으로 분리
iScore = []                    # 점수 리스트를 int로 형변환
total_new_score = 0            # 변환된 점수 총 합
max_score = 0                  # 최고 점수

# 최고점수 확인
for i in range(n):
    iScore.append(int(score[i]))
    if iScore[i] > max_score:
        max_score = iScore[i]

# 변환 된 점수 합계
for i in range(n):
    total_new_score = total_new_score + new_score(max_score, iScore[i])
    
avg_new_score = round(total_new_score / n,1)

print(avg_new_score)
