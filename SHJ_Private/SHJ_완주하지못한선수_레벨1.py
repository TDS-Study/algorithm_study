def solution(participant, completion):
    dParticipant = dict()

    # 참가자 해쉬 테이블에 입력 (동명이인에 대응하기 위해 Bool 대신 Int 사용)
    for p in participant:
        if p in dParticipant:
            dParticipant[p] += 1
        else:
            dParticipant[p] = 1

    # 완주자 카운트 -1
    for c in completion:
        dParticipant[c] += -1

    # 남아있는 사람
    for p in dParticipant:
        if dParticipant[p] == 1:
            answer = p
            break
    return answer


p = ["marina", "josipa", "nikola", "vinko", "filipa"]
c = ["josipa", "filipa", "marina", "nikola"]
solution(p,c)