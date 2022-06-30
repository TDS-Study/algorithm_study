
# import defaultdict module
from collections import defaultdict

n_of_pc = int(input())
n_of_links = int(input())
# 딕셔너리-셋 으로 그래프 구조 생성
g = defaultdict(set)
# 답이 들어갈 set
s = set()

for i in range(n_of_links):
    # 그래프에 데이터 입력
    # 1 2, 1 5, 5 7 인 경우
    # dic[1] = {2, 5}
    # dic[2] = {1}
    # dic[5] = {1, 7}
    a, b = map(int, input().split())    
    g[a].add(b)
    g[b].add(a)

# 깊이 우선 탐색으로 1부터 시작하는 전체 노드 탐색
def dfs(n, g):
    # 각 딕셔너리의 set 을 탐색
    for i in g[n]:
        if i not in s:
            s.add(i)
            dfs(i, g)

# 1로 시작하는 노드 전체 탐색
dfs(1, g)

# 1의 갯수를 제외하기 위해 -1 해줌
print(len(s)-1)
