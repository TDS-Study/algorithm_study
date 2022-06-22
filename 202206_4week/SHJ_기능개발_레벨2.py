'''
기능개발
'''

import math

def solution(progresses, speeds):
    days = []
    answer = []
    
    # 기능별 필요 작업 일수 계산
    for i in range(len(progresses)):
        days.append(math.ceil((100-progresses[i])/speeds[i]))
        
    # 기능 개발이 빨리 완료 되어도 앞기능 완료날 같이 배포 해야함
    # 앞뒤 기능 작업일수 계산하여 변경
    for i in range(1, len(progresses)):
        if days[i-1] > days[i]:
            days[i] = days[i-1]
    
    # 중복 제거 후 정렬 (set함수는 순서가 없음. days리스트의 index를 key로 정렬)
    unique_days = sorted(set(days), key=lambda x:days.index(x))
    
    # 작업일수 카운트해서 저장
    for day in unique_days:
        answer.append(days.count(day))
    return answer

# 입력
progresses = [93, 30, 55]
speeds = [1, 30, 5]

solution(progresses, speeds)