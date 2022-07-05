'''
타겟넘버
'''

def dfs(numbers, target, curr_v, sign,cnt):
    v = numbers.pop()
    if sign == '+': 
        curr_v += v
    else: curr_v -= v
    
    if len(numbers) >0:
        cnt = dfs(numbers.copy(), target, curr_v, '+',cnt)
        cnt = dfs(numbers.copy(), target, curr_v, '-',cnt)
    else:
        if curr_v == target:
            cnt = cnt+1
    
    return cnt
        
    
def solution(numbers, target):
    answer = 0
    
    answer = dfs(numbers.copy(), target, 0, '+',answer)
    answer = dfs(numbers.copy(), target, 0, '-',answer)
    return answer


n = [1,1,1,1,1]
t = 3
solution(n,t)