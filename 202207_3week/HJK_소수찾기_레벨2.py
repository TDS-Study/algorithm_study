# https://school.programmers.co.kr/learn/courses/30/lessons/42839

def mix(nums, temp):
    if len(nums) == 0:
        print(temp)
        temp = []
        return 
    
    for i in range(len(nums)):
        new_nums = nums.copy()
        new_nums.pop(i)
        temp += nums[i]
        mix(new_nums, temp)        
        print(str)        
    
    return

def solution(numbers):
    answer = 0
    nums = [x for x in numbers]
    combo = []
    # 숫자 조합 시작
    mix(nums, combo)
    
    return answer

numbers = "17123"
print(solution(numbers=numbers))