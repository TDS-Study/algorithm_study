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

t = int(input())
result = []

for i in range(t):
    # 수평 저장 리스트
    hl = []
    # 수직값 저장 리스트, 9개의 리스트를 가진 이중배열
    vl = [list() for _ in range(9)]
    sql = [list() for _ in range(9)]

    # 9 행을 읽는다
    for j in range(9):
        l = input().split()
        hl.append(l)

        for h in range(len(l)):
            vl[h].append(l[h])

print (hl)    
    
for i in range(t):

    for j in hl:
        # 1행에 유일한 아이템이 9개가 아니면 틀렸다
        if len(set(j)) != 9:
            result = False
            break
    
    # 행검사 후 결과
    if result == False:
        print(f'Case {i+1}: INCORRECT')
        #continue
    
    for j in vl:
        if len(set(j)) != 9:
            result = False
            break
    
    # 열검사 후 결과
    if result == False:
        print(f'Case {i+1}: INCORRECT')
        #continue

    for j in [0,3,6]:
        for h in [0,1,2]:
            for k in [0,3,6]:
                for l in [0,1,2]:
                    
                    sql[j+h].append(hl[k+l][k+l])
                
                

print(sql)






    


