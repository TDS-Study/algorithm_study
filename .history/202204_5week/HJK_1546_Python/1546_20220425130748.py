n = int(input())
ori_sc = [input() for _ in range(n)]
new_av = 100
sum = 0.0

if n > 1:
    max_sc = ori_sc[0]
    
    for i in range(0, n):
        if max_sc < ori_sc[i]:
            max_sc = ori_sc[i]
            
        sum += float(ori_sc[i])/n

    print("sum:",sum)
    print("max:",max_sc)
print(new_av)
