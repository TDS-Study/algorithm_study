
nTree, nLength = map(int, input().split())
lTrees = list(map(int, input().split()))

lTrees.sort()

begin, end = 1, max(lTrees)
middle = int
maxHeight = 0

while(begin <= end):
    middle = (begin + end) // 2
    sumLength = 0
    isPass = False

    for i in lTrees:
        if i >= middle:
            sumLength += (i-middle)

        if sumLength >= nLength:
            isPass = True
            break
    
    if isPass == True:
        begin = middle + 1
        maxHeight = middle
    else:
        end = middle - 1

print(maxHeight)

