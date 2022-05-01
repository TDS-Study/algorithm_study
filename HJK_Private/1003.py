import functools

t = int(input())
ns = map(int, [input() for _ in range(t)])

cnt0 = 0
cnt1 = 0

@functools.lru_cache
def fibonacci( n):
    global cnt0, cnt1
    if (n == 0):
        #rint("0")
        cnt0 += 1
        return 0
    
    elif (n == 1):
        #print("1")
        cnt1 += 1
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in ns:
    cnt0 = 0
    cnt1 = 0
    fibonacci(i)
    print(cnt0, " ", cnt1)

