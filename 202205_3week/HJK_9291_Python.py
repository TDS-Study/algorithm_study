"""문제
스도쿠는 일본어로 "수독(數獨)"을 읽은 것이다. 이는 미국에서 유명한 일본의 한 퍼즐 이름이기도 하다. 스도쿠는 9x9 격자판에 다음 조건을 만족하여 수를 채워 넣는 게임이다.

각 정수 1-9는 각 행에 정확히 한 번씩 등장해야 한다.
각 정수 1-9는 각 열에 정확히 한 번씩 등장해야 한다.
각 정수 1-9는 각 작은 3x3 정사각형에 정확히 한 번씩 등장해야 한다.
남규는 스도쿠에 푹 빠져서 하루종일 스도쿠 문제를 풀던 와중, 스도쿠를 풀었지만 그것이 정답인지를 쉽게 확인할 수 없어 고민에 빠졌다. 불쌍한 남규를 위해 다 채워진 스도쿠 판이 올바른 답인지 판별하는 프로그램을 작성해 주자.

입력
입력의 첫 줄에는 테스트 케이스의 개수가 주어진다.

각 테스트 케이스는 9개의 줄로 이루어져 있으며, 각 줄에는 9개의 정수가 공백으로 구분되어 있다. 각 정수는 1 이상 9 이하이다. 테스트 케이스의 사이에는 빈 줄이 하나 있다.

테스트 케이스의 개수는 100개를 넘지 않는다.

출력
각 테스트 케이스에 걸쳐 "Case x:"를 출력한 후, 공백 한 칸 뒤에 풀이가 올바르면 "CORRECT"를, 아니면 "INCORRECT"를 출력한다. x는 테스트 케이스 번호이며, 1부터 시작한다."""

# 반복할 횟수를 입력받는다
t = int(input())
# 결과 출력을 저장 할 변수
result = []

# 리스트를 넘겨받아 중복숫자가 있으면 False, 없으면 True 반환
def checkList(l):
    r = True

    for i in l:
        # Set 자료구조를 사용, 1개 행에 유일한 아이템이 9개가 아니면 틀렸다
        if len(set(i)) != 9:
            r = False
            break
    
    return r

def getInput():
    # 수평 값(행)) 저장 리스트
    hl = []
    # 수직 값(열)) 저장 리스트 초기화
    vl = [list() for _ in range(9)]
    # 3x3 스퀘어 저장 리스트 초기화
    sql = [list() for _ in range(9)]

    for i in range(9):
        l = input().split()
        # 수평 
        hl.append(l)

        for h in range(len(l)):
            # 각행의 수직 값 저장
            vl[h].append(l[h])

    # 3x3 스퀘어 리스트
    rowNum = 0
    # x 위치 시작점
    for x in [0,3,6]:
        # y 위치 시작점
        for y in [0,3,6]:
            
            for x1 in [0,1,2]:
                for y1 in [0,1,2]:
                    # 시작점 x,y 를 기준으로 3x3
                    sql[rowNum].append(hl[x+x1][y+y1])

            # 행번호는 0~8
            rowNum += 1   
    
    return hl, vl, sql
    
for i in range(t):

    h, v, sq = getInput()

    # 3개의 리스트 중 1개라도 틀린것이 있으면 틀림
    if checkList(h) == False or checkList(v) == False or checkList(sq) == False:
        result.append(f'Case {i+1}: INCORRECT')        
    else:
        result.append(f'Case {i+1}: CORRECT')

    # 한줄 건너 뜀
    if i != (t-1):
        input()

# 리스트 항목을 줄바꿈으로 분리하여 출력한다
print(*result, sep='\n')






    


