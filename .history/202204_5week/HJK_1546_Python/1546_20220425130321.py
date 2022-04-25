n = int(input())
ori_sc = [input() for _ in range(n)]
new_av = 100
sum = 0

if n > 1:
    max_sc = ori_sc[0]
    
    for i in range(0, n-1):
        
        sum += float(ori_sc[i])/n

        print(ori_sc[i])

print(new_av)
