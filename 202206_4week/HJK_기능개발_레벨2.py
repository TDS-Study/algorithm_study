def solution(progresses, speeds):
    answer = []
    while(sum(answer) < len(progresses)):
        cnt = 0
        for i in range(len(progresses)):
            # 첫 아이템이면 무관, 2번째 이후부터는 직전 아이템 값을 저장
            prev = -1 if i == 0 else progresses[i-1]

            # -1 이면 100을 넘기고 카운트에 더해진 후 이므로 무시
            if progresses[i] == -1:
                pass
            else:
                # -1 이 아닐 때 계속 더한다
                progresses[i] += speeds[i]

                # 직전 값이 -1 이면 100을 넘기고 카운트에 반영 되었으므로 
                # 자신의 카운트도 더하고 -1로 카운트 마쳤음을 표시
                if progresses[i] >= 100 and prev == -1:
                    cnt += 1
                    progresses[i] = -1
        
        if cnt > 0:
            answer.append(cnt)
        
    return answer

# p = [93, 30, 55]
# s = [1,30,5]

p = [95, 90, 99, 99, 80, 99]
s = [1, 1, 1, 1, 1, 1]

a = solution(p, s)

print(a)