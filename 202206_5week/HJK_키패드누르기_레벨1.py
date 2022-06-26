def get_dist(p_a:int, p_b:int):
    xlist = {"*": 1, "#": 3, 0:2, 1:1, 2:2, 3:3, 4:1, 5:2, 6:3, 7:1, 8:2, 9:3}
    ylist = {"*": 1, "#": 1, 0:1, 1:4, 2:4, 3:4, 4:3, 5:3, 6:3, 7:2, 8:2, 9:2}

    d1 = xlist[p_a] - xlist[p_b]
    d2 = ylist[p_a] - ylist[p_b]

    return abs(d1) + abs(d2)

def solution(numbers, hand):
    answer = ''
    usingHand = ''
    l_position = 0
    r_position = 0
    
    for i in numbers:
        if i in [1,4,7]:
            usingHand = 'L'
            l_position = i
        elif i in [3,6,9]:
            usingHand = 'R'
            r_position = i
        else:
            dist_from_left = get_dist(i, l_position)
            dist_from_right = get_dist(i, r_position)

            if dist_from_left < dist_from_right:
                

                usingHand = 'L'
                l_position = i
              
            elif dist_from_left > dist_from_right:
                usingHand = 'R'
                r_position = i
              
            else:
                if hand == 'left':
                    usingHand = 'L'
                    l_position = i
                else:
                    usingHand = 'R'
                    r_position = i
            
        answer += usingHand

    return answer


a = solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right')

print(a)