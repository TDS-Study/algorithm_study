def get_dist(a:int, b:int):
    # 숫자별 x, y 좌표를 딕셔너리로 저장
    xlist = {"*": 1, "#": 3, 0:2, 1:1, 2:2, 3:3, 4:1, 5:2, 6:3, 7:1, 8:2, 9:3}    
    ylist = {"*": 1, "#": 1, 0:1, 1:4, 2:4, 3:4, 4:3, 5:3, 6:3, 7:2, 8:2, 9:2}
    
    # x 좌표거리, y좌표거리 구함
    d1 = xlist[a] - xlist[b]
    d2 = ylist[a] - ylist[b]
    
    # 두 지점간 거리 반환
    return abs(d1) + abs(d2)

def solution(numbers, hand):
    answer = ''
    usingHand = ''
    l_position = '*'
    r_position = '#'
    
    for i in numbers:
        # 규칙1, 1,4,7은 왼손이 누른다
        if i in [1,4,7]:
            usingHand = 'L'
            l_position = i
        # 규칙2, 3,6,9는 오른손이 누른다
        elif i in [3,6,9]:
            usingHand = 'R'
            r_position = i
        else:
            # 거리를 구해서 비교한다
            dist_from_left = get_dist(i, l_position)
            dist_from_right = get_dist(i, r_position)

            if dist_from_left < dist_from_right:
                usingHand = 'L'
                l_position = i
            elif dist_from_left > dist_from_right:
                usingHand = 'R'
                r_position = i
            else:
                # 거리가 같은 경우 왼손잡이이면 왼손
                if hand == 'left':
                    usingHand = 'L'
                    l_position = i
                else:
                    usingHand = 'R'
                    r_position = i
            
        answer += usingHand

    return answer


a = solution([5,8,0], 'right')

print(a)