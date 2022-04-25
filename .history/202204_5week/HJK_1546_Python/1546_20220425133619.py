n = int(input())
ori_sc = [input() for _ in range(n)]
new_av = float(100)
avg = float(0)
max_sc = int(ori_sc[0])

if n > 1:        
    for i in range(0, n):
        o = int(ori_sc[i])
        if max_sc < o:
            max_sc = o
        avg += o/n
    new_av = avg / max_sc * 100
print(new_av)