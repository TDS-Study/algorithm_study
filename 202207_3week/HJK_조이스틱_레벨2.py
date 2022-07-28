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

def move_leftright(name, target, answer, direction):
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
    
    answer += dist
    # 위/아래 조작
    answer += move_updown(name, index)
    name[index] = "A"

    # 잘라서 시작위치가 0에 오게 만든다
    l = name[index:]
    r = name[:index]

    name = l + r
    
    # 모두 A 일 때 까지 계속 좌/우로 이동
    if name == target:
        return answer
    else:
         l = move_leftright(name.copy(), target, answer, "LEFT")
         r = move_leftright(name.copy(), target, answer, "RIGHT")

        # 좌/우 중 최소값을 리턴
         return l if l < r else r

def solution(name):
    answer = 0
    target = ["A" for _ in range(len(name))]
    name = [_ for _ in name]
    
    r = move_leftright(name.copy(), target, 0, "RIGHT")
    l = move_leftright(name.copy(), target, 0, "LEFT")

    answer = l if l < r else r
        
    return answer

name = "JEROEN"
name = "JAN"
name = "ABABAAAAABA"
name = "ABABAAAAABA"
print(solution(name))
