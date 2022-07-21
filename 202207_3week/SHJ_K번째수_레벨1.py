from re import A


def getKnum(l,commands):
    s = commands[0]
    e = commands[1]
    k = commands[2]
    
    l2 = l[s-1:e]
    l2.sort()
    return l2[k-1]
    
def solution(array, commands):
    answer = []
    for c in commands:
        answer.append(getKnum(array.copy(), c))
    print(answer)
    return answer


a = [1, 5, 2, 6, 3, 7, 4]
c =[[2, 5, 3], [4, 4, 1], [1, 7, 3]]	
solution(a, c)