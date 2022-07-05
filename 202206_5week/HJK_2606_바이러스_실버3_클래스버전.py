class Graph:
    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n+1)]

    def add(self, a, b):
        self.g[a].append(b)
        self.g[b].append(a)

    def dfs(self, start):
        return self.dfsv(start, set([start]))

    def dfsv(self, start, visited):
        for i in self.g[start]:
            if i not in visited:
                visited.add(i)
                self.dfsv(i, visited)
        return visited

n_of_pc = int(input())
n_of_links = int(input())
graph = Graph(n_of_pc)

for i in range(n_of_links):
    # 그래프에 데이터 입력
    a, b = map(int, input().split())
    graph.add(a, b)

# 1로 시작하는 노드 전체 탐색
visited = graph.dfs(1)

# print(visited)
# 1의 갯수를 제외하기 위해 -1 해줌
print(len(visited)-1)
