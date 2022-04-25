arr = [0] * (10010)

for i in range(9955, 10000):
    print("i:", i)

    txt = str(i)
    val = i

    for j in range(0, len(txt)):
        val += int(txt[j])
    print("val:",val)

    if val > 10003:
        break
    
    arr[val] = i
    

for idx, h in enumerate(arr[1:10000]):
    print(idx, " , " , h)
    #if h == 0:
    #    print(idx)