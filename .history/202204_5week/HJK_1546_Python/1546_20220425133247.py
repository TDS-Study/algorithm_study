n = int(input())
ori_sc = [int(input()) for _ in range(n)]
new_av = 100
avg = float(0)
max_sc = ori_sc[0]

try:
    if n > 1:        
        for i in range(0, n):
            o = ori_sc[i]
            if max_sc < o:
                max_sc = o
            avg += o/n
        new_av = avg / max_sc * 100
    print(new_av)
except EOFError as e:
    print(e)