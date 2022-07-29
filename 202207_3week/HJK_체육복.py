# https://school.programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    answer = n
    answer -= len(lost)

    lost.sort()
    lost2 = lost.copy()

    for i in lost:
        if i in reserve:
            reserve.remoge(i)
            answer += 1
            lost2.remove(i)
        
    for i in lost2:
        if i-1 in reserve:
            reserve.remove(i-1)
            answer += 1        
        elif i+1 in reserve:
            reserve.remove(i+1)
            answer += 1
    
    return answer



print(solution(3, [2,1], [2,3]))