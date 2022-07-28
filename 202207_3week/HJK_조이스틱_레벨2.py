# https://school.programmers.co.kr/learn/courses/30/lessons/42860

# AAA 를 LAZ 로 바꾸는 것이 아니라 LAZ 를 AAA 로 바꾸면서 셈한다.

def move_updown(name, current_index):
    dist = 0    
    current_char = name[current_index]
    
    if current_char >= 'N':
        dist = 91 - ord(current_char)
    else:
        dist = ord(current_char) - ord('A')
    
    return dist

def move_leftright(name, direction):
    dist = 0
    index = 0
    
    if direction == "LEFT":
        name_reverse = name[::-1]
        for i in range(len(name)):
            if name_reverse[i] != "A":
                dist = i + 1
                index = len(name) - dist
                break
    
    else: # RIGHT        
        for i in range(len(name)):
            if name[i] != "A":
                dist = i
                index = i
                break
        
        if dist_right <= dist_left:
            dist = dist_right
            index = index_right            
        else:
            dist = dist_left
            index = index_left

        answer += dist
        # 위/아래 조작
        answer += move_updown(name, index)
        name[index] = "A"
        l = name[index:]
        r = name[:index]
        
        name = l + r
    
    return dist, index

def solution(name):
    answer = 0
    all_a = ["A" for _ in range(len(name))]
    name = [_ for _ in name]
    
    current_index = 0
    
    
    dist, index = 0, 0
    dist_right, index_right = move_leftright(name.copy(), "RIGHT")
    dist_left, index_left = move_leftright(name.copy(), "LEFT")
        
        
    return answer

name = "JEROEN"
name = "JAN"
name = "ABABAAAAABA"
name = "ABABAAAAABA"
print(solution(name))
