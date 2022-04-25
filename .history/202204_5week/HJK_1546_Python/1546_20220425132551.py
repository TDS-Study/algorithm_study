n = int(input())
ori_sc = [float(input()) for _ in range(n)]
new_av = 100
avg = 0.0

try:
    if n > 1:
        max_sc = float(ori_sc[0])    
        for i in range(0, n):
            o = ori_sc[i]
            if max_sc < o:
                max_sc = o
            avg += o/n
        new_av = avg / max_sc * 100
    print(new_av)
except EOFError as e:
    print(e)