n = int(input())
ori_sc = [input() for _ in range(n)]
new_av = 100
sum = 0.0

if n > 1:
    max_sc = float(ori_sc[0])
    
    for i in range(0, n):
        o = float(ori_sc[i])
        
        if max_sc < o:
            max_sc = o
            
        sum += o/n

    print("sum:",sum)
    print("max:",max_sc)

    new_av = sum / max_sc

print("new av:", new_av)
