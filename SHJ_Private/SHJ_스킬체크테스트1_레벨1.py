def solution(s):
    sp = s.split(' ')
    
    answer = ''
    for string in sp:
        idx = 0
        for char in string:
            if idx == 0:
                answer += char.upper()
            else:
                answer += char.lower()
            idx = (idx + 1) % 2
        answer += ' '

    return answer[:-1]

s = "try hello world"
solution(s)