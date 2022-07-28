'''
가장 큰 수
# 반례: 중복 값이 들어갈 수 있음.
# 232, 23 처럼 비슷한데 자리수가 다른경우에 대한 처리.
'''
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def solution(numbers):
    answer = ''
    if sum(numbers) == 0:
        return '0'
    strN =[]
    for n in numbers:
        n2 = str(n)
        if len(n2) ==1:
            strN.append([n2, n2+n2+n2+n2])
        elif len(n2) ==2:
            strN.append([n2, n2+n2])
        elif len(n2) ==3:
            strN.append([n2, n2+n2[0]])
        else:
            strN.append([n2, n2])

    nKeys =sorted(strN, key = lambda x:x[1], reverse=True)

    for n in nKeys:
        answer +=n[0]
    print(answer)
    return answer

# n= [101, 10]
# n= [232, 23]
n= [101, 10, 232, 23,23] #2323210110 
# n = [3, 30, 34, 5, 9]
# n =[]
# for i in range(0,1001):
    # n.append(i)
solution(n)

