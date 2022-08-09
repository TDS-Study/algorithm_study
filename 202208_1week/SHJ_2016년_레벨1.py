def solution(a, b):
    answer = ''
    
    dayByMonth = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dayByWeek = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    
    days = sum(dayByMonth[:a])+b # 1월1일 ~ a월b일의 총 일수 계산
    answer = dayByWeek[days%7-1] # dayOfWeek 리스트의 index 맞추가 위해 -1. 
    
    return answer