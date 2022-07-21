'''
Dead Or Arrive
'''
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
class CarInfo:
    w = int()
    idx = int()
    def __init__(self, w, idx):
        self.w = w
        self.idx = idx

def solution(n, car_info):
    cars = {}
    for i in range(n):
        v, w = car_info[i].split()        
        if v in cars:
            if cars[v].w <= w:   # 새로 들어온 차의 내구성이 더 크면 변경
                cars[v] = CarInfo(w, i+1)
        else:
            cars[v] = CarInfo(w, i+1)
        
    answer = 0
    for v in cars.values():
        answer += v.idx         # 차량 번호 더하기
    print(answer)
    

# case 1
n = 5
car_info = ['1 5','5 10','3 20','3 15','3 25']

# case2
n = 7
car_info = ['1 10','2 25','3 25','3 30','3 35','2 30', '2 50']

n =5
car_info = ['1 50', '2 10', '1 50', '3 10', '3 10']
solution(n,car_info)
