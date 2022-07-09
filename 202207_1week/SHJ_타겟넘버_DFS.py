'''
타겟넘버

함수의 매개변수 전달
* pass by value     : 변수의 값을 복사하여 함수에 전달. return하여 재 할당 해줘야함.
* pass by reference : 변수의 주소를 전달하여 직접 변경함. return으로 재할당 하지 않아도 됨.
                    ex) list, dictionary)


ex) pass by reference
def plus(list):
    list[0] += 1

t = [10]
plus(t)
print(t) 
>>> [11]

ex) pass by value
def plus(list):
    list += 1
    return list

t = 10
t = plus(t)
print(t) 
>>> [11]
link: https://hongl.tistory.com/259
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