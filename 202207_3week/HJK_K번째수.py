# https://school.programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []

    for com in commands:
        i, j, k = [x-1 for x in com]
        j += 1  

        new_arr = array[i:j]
        new_arr.sort()
        
        answer.append(new_arr[k])

    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))