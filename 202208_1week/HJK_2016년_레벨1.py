# https://school.programmers.co.kr/learn/courses/30/lessons/12901

def solution(a, b):
    answer = ''    
    # 2016년 1월1일이 금요일이라 FRI 부터 시작함
    # 1월 1일이 주어지면 총 지난 일수 1 / 7 의 나머지가 1 이다
    # 인덱스는 0부터 시작하므로 1을 빼면 0번째 FRI 가 나오도록 한다
    date_names = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    # 윤년이라 2월이 29개일 있음
    days_by_month_leapyear = [31,29,31,30,31,30,31,31,30,31,30,31]       
    # 5월 24일이 주어지면 1~4월까지 날짜 갯수(121) + 주어진 b(24) 를 더해서 1월1일부터 총 일수를 구함
    # 5월 24일 -> 121 + 24 = 145,  145 / 7 의 나머지 = 5
    day_sum = sum(days_by_month_leapyear[0:a-1]) + b
    # 요일 목록에서 앞에 구한 나머지 5 - 1 = 4 해서 인덱스 구함
    answer = date_names[day_sum % 7 - 1]
    
    return answer

print(solution(5, 24))
print(solution(12, 31))