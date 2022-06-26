def solution(numbers, hand):
    answer = ''
    hand = ''
    for i in numbers:
        if i in [1,4,7]:
            hand = 'left'
        elif i in [3,6,9]:
            hand = 'right'
        else:
            hand = 'left'

        answer += hand

    return answer


a = solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right')

print(a)