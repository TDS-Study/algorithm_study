'''
소수찾기 레벨1 - 에라토스테네스의 체
2는 사용, 2의 배수 제거
3은 사용, 3의 배수 제거.....
'''
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def solution(n):
    answer = 0
    num = set(range(2,n+1))
    
    for i in range(2,n+1):
        if i in num:
            num -= set(range(2*i, n+1, i))
                
    return len(num)

solution(100)