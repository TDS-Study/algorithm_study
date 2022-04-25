n = int(input())
ori_sc = [input() for _ in range(n)]
new_sc = []

new_avg = 100

if n > 1:
    max_sc = ori_sc[0]
    
    for i in range(0, n-1):
        print(ori_sc[i])

print(new_avg)
