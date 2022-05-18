# 1072번 게임
from ast import Import
from pickle import TRUE
from decimal import Decimal
import random

def checkRight(x, y, z, idx, f, l):
    z1 = (y+idx-1)*100 // (x+idx-1)
    z2 = (y+idx)*100 // (x+idx)
    z3 = (y+idx+1)*100 // (x+idx+1)

    if z1+1 == z2 and z == z1:
        return idx# print('')
    elif z2+1 == z3 and z == z2:
        return idx +1
    else:
        return idx
        # print('this is hole !!')

def bisearch(x, y, z):
    f = 0
    l = x
    while f <= l:
        idx = (f + l) // 2
        zTemp = (y+idx)*100//(x+idx)
        if l-f <= 1:
            if zTemp > z:
                idx = checkRight(x, y, z, idx, f, l)
                return idx
            else: 
                idx = checkRight(x, y, z, idx+1, f, l)
                return idx
        if zTemp > z:
            l = idx-1
        else:
            f = idx+1
    return -1

def main(x, y):
    if x == y:
        print(-1)
        return

    z = y*100 //x

    if z == 99:
        print(-1)
        return
           
    print(bisearch(x, y, z))

if __name__ == "__main__":
    x, y = map(Decimal, input().split())
    main(x, y)

    # while (True):
    #     x= random.randrange(1,999999)
    #     y = random.randrange(0,x)
    #     main(x, y)
