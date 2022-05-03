arr = [0] * (10010)

for i in range(1, 10000):
    val = i

    for j in str(i):
        val += int(j)

    if val > 10003:
        break
    
    arr[val] = 1    

for idx, h in enumerate(arr[0:10000]):
    if idx != 0 and h == 0:
        print(idx)
