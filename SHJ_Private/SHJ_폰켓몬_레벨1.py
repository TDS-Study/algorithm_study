def solution(nums):
    answer = 0
    sNums = set(nums)
    cnt = len(nums)
    if len(sNums) > cnt/2:
        answer = cnt/2
    else:
        answer = len(sNums)
    return answer