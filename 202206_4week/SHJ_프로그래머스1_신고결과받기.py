'''
신고 결과 받기
'''

def solution(id_list, report, k):
    sReport = set(report)   # 중복 제거
    dReport ={}             # dictionary로 변경
    dId_list = {}           # dictionary로 변경

    for _ in id_list:
        dId_list[_] = 0

    for item in sReport:                         # dReport = {신고당한사람 : 신고한 사람1, 신고한 사람2 ... }
        temp = item.split()
        if temp[1] in dReport.keys():            # 리스트에 인덱스 추가
            dReport[temp[1]].append(temp[0])
        else:                                    # 최초 입력시 리스트로 인덱스 추가
            dReport[temp[1]] = []
            dReport[temp[1]].append(temp[0])
    
    for key, value in dReport.items():           # 신고한 사람 개수가 많으면 id list에 숫자 추가
        if len(value) >= k:
            for _ in value:
                dId_list[_] += 1

    answer = []
    for _ in dId_list.values():
        answer.append(_)
    
    return answer



# id_list = ["con", "ryan"]
# report = ["ryan con", "ryan con", "ryan con", "ryan con"]
id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

solution(id_list, report, k)