from dataclasses import dataclass

@dataclass
class Position:
    x: int
    y: int
    
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

def solution(maze, queries):
    answer = []
    
    for i in queries:
        params = i.split()
        # 출발점, 좌표계 변환을 위해 -1 해준다
        start = Position(int(params[0])-1, int(params[1])-1)
        # 도착점, 좌표계 변환을 위해 -1 해준다
        finish = Position(int(params[2])-1, int(params[3])-1)
        # 이동 가능한 알파벳을 리스트로 변환
        available_block = [j for j in params[4]]
        
        path = []        
        path.append(start)
                
        # 현재 위치에서 이동 가능한 알파벳으로 이동
        # 도착점에 도착한 경우 총 이동거리를 반환
        # 도착점에 도착하지 못한 경우 -1 반환
        p = move(path, available_block, maze, finish)
        
        print(p)

    return answer

def move(path, available_block, maze, finish) -> list:
    # 현재 위치
    p_c = path[-1]
    
    path = list(path)
       
    if p_c == finish:
        return path
    else:
        p1 = Position(p_c.x+1, p_c.y) # 오른쪽으로 1칸
        p2 = Position(p_c.x, p_c.y+1) # 아래쪽으로 1칸
        p3 = Position(p_c.x-1, p_c.y) # 왼쪽으로 1칸
        p4 = Position(p_c.x, p_c.y-1) # 위쪽으로 1칸   
        path1, path2, path3, path4 = [], [], [], []     
        
        # 이동 가능한 알파벳으로 이동
        if p1 not in path and p1.x >= 0 \
        and p1.x < len(maze) \
        and p1.y >= 0 \
        and p1.y < len(maze[0]) \
        and maze[p1.x][p1.y] in available_block:
            path.append(p1)
            path1 = move(path, available_block, maze, finish)
            print(path1)
        
        if p2 not in path and p2.x >= 0 \
        and p2.x < len(maze) \
        and p2.y >= 0 \
        and p2.y < len(maze[0]) \
        and maze[p2.x][p2.y] in available_block:
            path.append(p2)
            path2 = move(path, available_block, maze, finish)
            print(path2)
        
        if p3 not in path and p3.x >= 0 \
        and p3.x < len(maze) \
        and p3.y >= 0 \
        and p3.y < len(maze[0]) \
        and maze[p3.x][p3.y] in available_block:
            path.append(p3)
            path3 = move(path, available_block, maze, finish)
            print(path3)
        
        if p4 not in path and p4.x >= 0 \
        and p4.x < len(maze) \
        and p4.y >= 0 \
        and p4.y < len(maze[0]) \
        and maze[p4.x][p4.y] in available_block:
            path.append(p4)
            path4 = move(path, available_block, maze, finish)
            print(path4)
    
        # 이동 가능한 알파벳으로 이동하지 못한 경우
        if path1 == [] and path2 == [] and path3 == [] and path4 == []:
            return []
        
        minLength = max(len(path1), len(path2), len(path3), len(path4))
        for i in [path1, path2, path3, path4]:
            if len(i) == 0:
                continue
            elif len(i) < minLength:
                minLength = len(i)                
                path = i
        
    return path


m = ["AAAAA",
     "AABBB",
     "CAEFG",
     "AAEFF"]
q = ["1 5 4 5 ABF"]

a = solution(m, q)
print(a)