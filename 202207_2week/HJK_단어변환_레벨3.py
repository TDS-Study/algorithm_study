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

# 두 단어가 하나의 차이만 있는지 확인한다
def is_one_diff(word1, word2):
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1
        if count > 1:
            return False
    return True

def dfs(l, start, target, visited, min_visited):
    # 경로에 노드 추가
    visited.append(start)

    # 도착했으면 경로를 반환한다
    if start == target:
        return visited
    
    # 도착하지 않은 경우 자식 노드를 방문한다
    for i in l[start]:
        # 이미 방문한 노드는 가지 않는다
        if i not in visited:
            # 자식노드에서 타겟까지 간 경우 비어있지 않은 경로를 반환한다
            v = dfs(l, i, target, visited.copy(), [])

            # 타겟까지 못간경우는 무시하고 다음 자식노드를 탐색
            if v == []:
                continue
            
            # 자식들의 경로 중 짧은 것만 min_visited에 보관한다
            if min_visited == [] or len(v) < len(min_visited):
                min_visited = v

    # 자식노드 탐색 결과가 있으면 반환한다
    if min_visited != []:
        return min_visited

    return []
def solution(begin, target, words):
    answer = 0
        
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
    
    # 그래프를 dfs로 탐색한다
    # bfs(l, begin, target)

    # dfs 로 탐색한다
    visited = dfs(l, begin, target, [], [])
    
    return 0 if visited == [] else len(visited)-1


if __name__ == '__main__':
    
    begin = "hit"
    target = "cog"
    words = ["hot", "dot", "dog", "lot", "log", "cog"]
    words = ["hot", "dot", "dog", "lot", "log"]
    print(solution(begin, target, words))