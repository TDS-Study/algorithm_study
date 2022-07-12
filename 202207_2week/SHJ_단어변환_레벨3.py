'''
단어변환
'''

from collections import deque

def checkWord(word1, word2):
    diffChar =0
    for i in range(len(word1)):
        if word1[i]!= word2[i]:
            diffChar +=1
    
    if diffChar ==1:    # 단어 전체 비교하여 차이가 1개면 변환 가능.
        return True
    else: return False

def possibleWord(curWord, words, queue, visit):
    if '1' not in queue:    # 1이 있을때 depth를 추가함.
        queue.append('1')

    for w in words:
        if visit[w]:        # 방문하지 않는 경우만 체크
            continue
        if checkWord(curWord, w):   # 변경 가능한지 체크
            queue.append(w)
    
    return queue

def bfs(begin, target, words):
    visit = {}
    for x in words:
        visit[x] = False
    
    depth = 0
    queue = deque([begin])
    while queue:
        cur_word =  queue.popleft()
        if cur_word == target:  # 목적지 도착
            return depth
        if cur_word == '1':     # depth 증가
            depth += 1
            continue
        visit[cur_word] = True  # 방문.
        queue = possibleWord(cur_word, words, queue,visit)  # 가능한 리스트 추가
    return 0    # words 리스트에 target은 있으나 변환할 수 없는 경우
    
def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    answer = bfs(begin, target, words)

    return answer


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log"]
solution(begin, target, words)

