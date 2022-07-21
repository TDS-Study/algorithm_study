def solution(n, lost, reserve):
    answer = 0
    
    # 여벌 체육복을 가져온 학생이 도난당했을 경우 처리.
    for i in reserve.copy():
        if i in lost.copy():
            reserve.remove(i)
            lost.remove(i)
    
    # 앞뒤 순서대로 비교하기 위해 정렬
    reserve.sort()
    lost.sort()
    
    isNum = [False for i in range(n+1)]
    
    # 여벌 체육복 있는지 확인
    for i in reserve:
        isNum[i] = True

    for i in lost.copy():
        if 1 < i < n:
            if isNum[i-1]:
                lost.remove(i)
                isNum[i-1] = False
            elif isNum[i+1] :
                lost.remove(i)
                isNum[i+1] = False
        elif 1 < i:     # 처음 값
            if isNum[i-1]:
                lost.remove(i)
                isNum[i-1] = False
        elif i < n:     # 마지막 값
            if isNum[i+1] :
                lost.remove(i)
                isNum[i+1] = False
    
    
    answer = n - len(lost)
    
    return answer