max = 100

arr = []
arr.append(0)
prev_val = 0

for i in range(1, max):
    print("i:", i)

    txt = str(i)
    val = i

    for j in range(0, len(txt)):
        val += int(txt[j])
        # print("val:",val)

    if val - prev_val > 1:
        for h in range(0, val - prev_val - 1):
            arr.append(0)
            # print("added")
        
    if val > max:
        break

    arr.append(val)

    prev_val = val


for idx, h in enumerate(arr):
    print(idx, " and " , h)
    
