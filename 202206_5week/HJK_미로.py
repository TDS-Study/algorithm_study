from dataclasses import dataclass

@dataclass
class Position:
    row: int
    col: int
    
    def __init__(self, r: int, c: int):
        self.row = r
        self.col = c

def solution(maze, queries):
    answer = []
    new_maze = [0 for _ in range(len(maze)+1)]
    row_length = len(maze)
    col_length = len(maze[0])
    
    for i in maze[0]:
        new_maze[0] = str(new_maze[0]) + "0"

    for i in range(1, len(maze)+1):
        new_maze[i] = "0" + maze[i-1]

    # 좌표를 변환 필요없게 더미 행,열 추가    
    #             000000
    # AAAAA       0AAAAA
    # AABBB   ->  0AABBB    
    # CAEFG       0CAEFG
        
    for i in queries:
        params = i.split()
        # 출발점
        start = Position(int(params[0]), int(params[1]))
        # 도착점
        finish = Position(int(params[2]), int(params[3]))
        # 이동 가능한 알파벳
        available_block = params[4]
        
        path = []
        path.append(start)
                
        # 현재 위치에서 이동 가능한 알파벳으로 이동
        # 도착점에 도착한 경우 총 이동거리를 반환
        # 도착점에 도착하지 못한 경우 -1 반환
        p = move(path, available_block, new_maze, finish, row_length, col_length)
        
        print(p)

        if p == []:
            answer.append(-1)
        else:
            answer.append(len(p))

    return answer

def move(path, available_block, maze, finish, row_length, col_length) -> list:
    # 현재 위치
    c_p = path[-1]
    path = list(path) # 새로운 list 객체 생성
        
    if c_p == finish:
        return path
    else:
        RIGHT = Position(c_p.row, c_p.col+1) # 오른쪽으로 1칸
        DOWN = Position(c_p.row+1, c_p.col) # 아래쪽으로 1칸
        LEFT = Position(c_p.row, c_p.col-1) # 왼쪽으로 1칸
        UP = Position(c_p.row-1, c_p.col) # 위쪽으로 1칸   
        path_right, path_down, path_left, path_up = [], [], [], []

        # 이미 지나온 길은 못감
        # 행, 열 번호가 1~길이 사이 인 경우만 가능
        # 이동 가능한 알파벳 목록에 있는 경우만 가능

        # 오른쪽으로 이동        
        if RIGHT not in path \
        and RIGHT.row >= 1 and RIGHT.row <= row_length \
        and RIGHT.col >= 1 and RIGHT.col <= col_length \
        and maze[RIGHT.row][RIGHT.col] in available_block \
        :
            new_path = list(path)
            new_path.append(RIGHT)
            path_right = move(new_path, available_block, maze, finish, row_length, col_length)            
        
        # 아래쪽으로 이동
        if DOWN not in path \
        and DOWN.row >= 1 and DOWN.row <= row_length \
        and DOWN.col >= 1 and DOWN.col <= col_length \
        and maze[DOWN.row][DOWN.col] in available_block \
        :
            new_path = list(path)
            new_path.append(DOWN)
            path_down = move(new_path, available_block, maze, finish, row_length, col_length)            
        
        # 왼쪽으로 이동
        if LEFT not in path \
        and LEFT.row >= 1 and LEFT.row <= row_length \
        and LEFT.col >= 1 and LEFT.col <= col_length \
        and maze[LEFT.row][LEFT.col] in available_block \
        :
            new_path = list(path)
            new_path.append(LEFT)
            path_left = move(new_path, available_block, maze, finish, row_length, col_length)            
        
        # 위쪽으로 이동
        if UP not in path \
        and UP.row >= 1 and UP.row <= row_length \
        and UP.col >= 1 and UP.col <= col_length \
        and maze[UP.row][UP.col] in available_block \
        :
            new_path = list(path)
            new_path.append(UP)
            path_up = move(new_path, available_block, maze, finish, row_length, col_length)            
    
        # 이동 가능한 알파벳이 없는 경우(막다른길)
        if path_right == [] and path_down == [] and path_left == [] and path_up == []:
            return []
        
        # 이동한 경로 중 최소 경로만 반환
        minLength = 10000 # 가능한 최대 이동 = 100 * 100
        for i in [path_right, path_down, path_left, path_up]:
            if len(i) == 0:
                continue
            elif len(i) <= minLength:
                minLength = len(i)
                path = i
        
    return path

m = ["AAAAA",
     "AABBB",
     "CAEFG",
     "AAEFF"]
q = [
    "1 1 1 5 AF",
     "1 1 4 5 AF",
     "2 1 4 5 FAE",
     "1 5 4 5 ABF",
     "1 1 4 1 A"]
# m = ["AAA",
#      "ABB",
#      "ABA"]
# q = [
#     "1 1 1 3 A",
#      "1 3 3 1 A",
#      "1 1 3 3 A",     
#      "1 1 3 3 AB"]
a = solution(m, q)
print(a)