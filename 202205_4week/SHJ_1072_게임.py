# 1072번 게임
from decimal import Decimal
import math
def bisearch(x, y, z):
    s = 1
    e = x
    mid = 0
    while s < e:
        mid = (s + e) // 2
        zTemp = math.trunc((y+mid)*100/(x+mid))
        
        if zTemp > z:
            e = mid-1
        else:
            s = mid+1
    return mid

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
        # x= random.randrange(1,999999)
        # y = random.randrange(0,x)
        # main(x, y)