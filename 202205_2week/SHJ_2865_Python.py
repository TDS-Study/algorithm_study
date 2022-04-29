# 2865번 나는 위대한 슈퍼스타 K
# 메모리 30840 KB
# 시간 76 ms

n, m, k=map(int, input().split(' ')) # n: 참가자수, m: 장르수, k: 본전 진출자

mList = [0]*(n+1)                    # 각 참가자의 최고 점수만 입력하자 (*참가번호는 1번부터 시작하므로 n+1 해줌)

for iM in range(m):
    tempList = input().split(' ')    # 장르별 참가번호, 점수 자르기
    for iN in range(0, n*2,2):    
        i = int(tempList[iN])        # i: 참가번호
        s = float(tempList[iN+1])    # s: 점수
        if mList[i] < s :            # 기존 점수보다 새 장르의 점수가 크면 큰 점수로 변경
            mList[i] = s


mList.sort(reverse=True)             # 내림차순 정렬 (*리스트.sort() 기본은 오름차순 정렬)

# 합격자 수만큼 더하기
total = 0
for i in range(0,k):
    total = total + mList[i]

print(round(total,1))                # 소수점 첫째자리까지 반올림해서 제출!!!!!
