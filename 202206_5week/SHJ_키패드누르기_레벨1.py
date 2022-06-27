'''
키패드누르기
'''

def getDist(fromP, toP):        # 키패드 사이의 거리 구하기
    diff = abs(fromP - toP)
    return diff//3 + diff%3  

def checkN(answer, hand, lastN, n):     # 2, 5, 8, 0(11) 위치일 때 입력 문자열 판단
    leftN = getDist(lastN['L'], n)
    rightN = getDist(lastN['R'], n)

    if leftN == rightN:
        answer += hand
        lastN[hand]= n
    elif leftN < rightN:
        answer += 'L'
        lastN['L'] = n
    else:
        answer += 'R'
        lastN['R'] = n

    return answer, lastN

def solution(numbers, hand):
    answer = ''
    
    hand = hand[:1].upper()
    lastN = {'L':10, 'R':12}
            
    for n in numbers:
        if n == 0:
            answer, lastN = checkN(answer, hand,lastN, 11)
        elif n%3 == 2:
            answer, lastN = checkN(answer, hand,lastN, n)
        elif n%3 == 1:
            answer += 'L'
            lastN['L'] = n
        else:
            answer += 'R'
            lastN['R'] = n
    
    return answer


solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right')