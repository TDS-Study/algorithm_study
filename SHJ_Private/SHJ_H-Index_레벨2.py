'''
H-index
'''
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def solution(citations):
    answer = 0
    
    citations.sort(reverse = True)
    for i in range(len(citations)):
        if i == len(citations)-1 and citations[i] >= i+1:
            answer = i+1
            break
        # index로 볼때 for문을 더 돌면 답이 나올 수 없는 경우.
        elif i+1 < len(citations) and citations[i] >= i+1 and citations[i+1] <= i+1:
            answer = i+1
            break
    return answer

n= [7, 7, 0,0]

solution(n)

