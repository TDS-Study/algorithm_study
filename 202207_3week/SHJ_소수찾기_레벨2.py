'''
소수찾기 레벨2
'''
from itertools import permutations

def isPrimeNumber(n):
    if n <2:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    nums = []
    for l in range(1, len(numbers)+1):
        nums.append([''.join(i) for i in list(permutations(list(numbers),l))])
    
    nums_all = []
    for n in nums:
        nums_all.append(n)
    nums = set()
    for i in nums_all:
        for i2 in i:
            nums.add(int(i2))

    
    for n in set(nums):
        bResult = isPrimeNumber(n)
        if bResult:
            answer += 1
    return answer

solution("011")