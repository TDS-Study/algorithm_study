'''
바이러스 - DFS 
'''

def solution(pairs):
    answer = set()  # 중복 제거를 위해 set 사용
    answer.add(1)

    # 5
    # 4         
    # 1 2  (1) -> (1, 2, 5) -> (1, 2, 3, 5) -> (1, 2, 3, 4, 5)
    # 3 4
    # 1 5
    # 2 3

    for i in range(pair-1):       # 쌍 개수-1 만큼 반복 (6개 쌍이 한번에 하나씩 합쳐지면 최대 5번이 필요함)
        tmp_answer = set()        # 해당하는 값을 임시로 저장하기 위한 set
        for a in answer:          # 정답 리스트의 원소 1개씩 for문 (ex. answer = [1, 2, 5]라면 각각 loop)
            i = 0
            while i < len(pairs):
                if a in pairs[i]:
                    tmp_answer.update(pairs.pop(i))
                else:
                    i += 1
        answer.update(tmp_answer)   # set에 리스트 추가하기
    print(len(answer)-1)
         
computer = int(input())
pair = int(input())
pairs = []
for i in range(pair):
    pairs.append(list(map(int, input().split())))

solution(pairs)