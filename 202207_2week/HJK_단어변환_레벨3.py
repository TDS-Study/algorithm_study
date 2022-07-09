"""문제 설명
두 개의 단어 begin, target과 단어의 집합 words가 있습니다. 아래와 같은 규칙을 이용하여 begin에서 target으로 변환하는 가장 짧은 변환 과정을 찾으려고 합니다.

1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
2. words에 있는 단어로만 변환할 수 있습니다.
예를 들어 begin이 "hit", target가 "cog", words가 ["hot","dot","dog","lot","log","cog"]라면 "hit" -> "hot" -> "dot" -> "dog" -> "cog"와 같이 4단계를 거쳐 변환할 수 있습니다.

두 개의 단어 begin, target과 단어의 집합 words가 매개변수로 주어질 때, 최소 몇 단계의 과정을 거쳐 begin을 target으로 변환할 수 있는지 return 하도록 solution 함수를 작성해주세요.

제한사항
각 단어는 알파벳 소문자로만 이루어져 있습니다.
각 단어의 길이는 3 이상 10 이하이며 모든 단어의 길이는 같습니다.
words에는 3개 이상 50개 이하의 단어가 있으며 중복되는 단어는 없습니다.
begin과 target은 같지 않습니다.
변환할 수 없는 경우에는 0를 return 합니다."""
# https://school.programmers.co.kr/learn/courses/30/lessons/43163

# start 부터 target 까지 그래프로 연결가능하면 경로의 길이를 반환한다
# 최소 경로가 필요하므로 bfs 를 사용한다

# 두 단어가 하나의 차이만 있는지 확인한다
def is_one_diff(word1, word2):
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1
        if count > 1:
            return False
    
    return True

def bfs(l, begin, target):
    queue = [begin]
    visited = []
    cnt = 0
    while queue:
        word = queue.pop(0)
        
        if word == target:
            return True
        visited.append(word)
        for i in l[word]:
            if i not in visited:
                queue.append(i)
        cnt += 1
        
    return False

def solution(begin, target, words):
    answer = 0
    
    # 타겟도 words 에 넣어준다
    words.append(target)
    
    # 그래프를 저장 할 딕셔너리
    l = {}
    l[begin] = []
    
    while words:
        # 단어 하나씩 뽑아서 그래프에 추가한다
        word = words.pop()
        l[word] = []
        
        for i in l:
            # 같은 경우는 패스
            if word == i:
                continue
            
            # 한글자만 다른 경우 연결해준다
            if is_one_diff(word, i):                
                
                if i not in l[word]:
                    l[word].append(i)
                
                if i not in l[i]:
                    l[i].append(word)
    
    # 그래프를 bfs로 탐색한다
    bfs(l, begin, target)    
    
    return answer


if __name__ == '__main__':
    
    begin = "hit"
    target = "cog"
    words = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(solution(begin, target, words))