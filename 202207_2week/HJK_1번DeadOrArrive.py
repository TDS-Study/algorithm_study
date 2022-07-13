
# 속도의 최대값
MAX_V = 1001

car_list = [[1,50], [5,10], [3,20], [3,15], [3,25]]
car_list = [[1,10], [2,25],[3,25],[3,30],[3,35],[2,30],[2,50]]
n_cars = len(car_list)

# 각 속도를 인덱스로 가지는 리스트 초기화
# answer[500] 은 속도가 500인 차량을 의미함
answer = [ 0 for _ in range(MAX_V) ]

for i in range(n_cars):    
    v = car_list[i][0]
    w = car_list[i][1]

    # 해당 속도의 차량 중 내구도가 가장 큰 차량의 번호를 저장
    # answer[500] 인 차량의 내구도 w 가 기존 내구도보다 크거나 같으면 순번을 넣는다
    # 동일할때는 뒷순번으로 갈수록 덮어쓰므로 순번이 큰 것이 자연히 저장됨
    if answer[v] <= w:
        answer[v] = i + 1

# 리스트 전체 합 출력
print(sum(answer))