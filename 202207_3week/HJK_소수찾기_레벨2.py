# https://school.programmers.co.kr/learn/courses/30/lessons/42839

def is_prime(n):
    # 1 이하는 소수가 아님
    if n <= 1:
        return False
    # 2부터 루트 n 까지 나누어 떨어지는 지 확인
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False
    return True

def make_combination(nums, temp, result):
    for i in range(len(nums)):
        # 숫자 조합이 소수 이면 result 에 추가
        # set 을 사용하여 중복 방지
        if is_prime(int(temp + str(nums[i]))):
                result.add(int(temp + str(nums[i])))

        if len(nums) == 1:
            # 마지막 수이면 종료
            return
        else:
            # 현재 사용하는 수는 제외하고 재귀호출
            new_nums = nums.copy()
            new_nums.pop(i)
            # 남은 수들로 재귀호출 한다
            make_combination(new_nums, temp + nums[i], result)
    
    return

def solution(numbers):
    answer = 0
    nums = [x for x in numbers]
    result, temp = set(), ""
    # 숫자 조합 시작
    make_combination(nums, temp, result)

    answer = len(result)
    
    return answer

numbers = "011"
print(solution(numbers=numbers))