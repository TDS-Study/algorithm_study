

def solution(maze, queries):
    answer = []

    for i in queries:
        params = i.split()
        # 출발점, 좌표계 변환을 위해 -1 해준다
        start = [int(params[0])-1, int(params[1])-1]        
        # 도착점
        finish = [int(params[2])-1, int(params[3])-1]
        # 이동 가능한 알파벳을 리스트로 변환
        available_block = [j for j in params[4]]

        # 현재 위치에서 이동 가능한 알파벳으로 이동
        # 도착점에 도착한 경우 총 이동거리를 반환
        # 도착점에 도착하지 못한 경우 -1 반환


    return answer

def move(start, path, ):



    return -1


m = ["AAAAA","AABBB","CAEFG","AAEFF"]
q = ["1 5 4 5 ABF"]

a = solution(m, q)
print(a)