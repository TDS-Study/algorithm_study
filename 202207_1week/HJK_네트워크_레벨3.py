"""문제 설명
네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다. 예를 들어, 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고, 컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때 컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다. 따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.

컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 네트워크의 개수를 return 하도록 solution 함수를 작성하시오.

제한사항
컴퓨터의 개수 n은 1 이상 200 이하인 자연수입니다.
각 컴퓨터는 0부터 n-1인 정수로 표현합니다.
i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현합니다.
computer[i][i]는 항상 1입니다."""

# https://school.programmers.co.kr/learn/courses/30/lessons/43162


class Graph:
    def __init__(self, n):
        self.n = n
        self.g = [set() for _ in range(n)]

    def add(self, a, b):
        self.g[a].add(b)

    def bfs(self, start):
        visited = []
        queue = [start]

        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.append(node)
                queue.extend(self.g[node])

        return visited


def solution(n, computers):
    answer = 0
    graph = Graph(n)
    # 그래프에 데이터 입력
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i != j:
                graph.add(i, j)
                graph.add(j, i)

    # 0 부터 n-1 번 pc 까지 들러야 하는 전체 대상을 정의
    # 예) n = 4 일때 [0, 1, 2, 3] 모두 4개의 pc를 다 들러야 한다
    to_visit = [i for i in range(n)]

    while to_visit:
        # bfs 를 이용해 연결 된 노드들을 방문하고 결과를 리턴
        visited = graph.bfs(to_visit[0])
        # 네트워크 카운트 증가
        answer += 1

        # 방문한 노드들을 to_visit에서 제거
        for i in visited:
            if i in to_visit:
                to_visit.remove(i)

    return answer


n = 10
computers = [[1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
             [0, 1, 0, 0, 0, 0, 1, 1, 0, 1],
             [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
             [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
             [1, 1, 0, 0, 0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
             [0, 1, 0, 0, 0, 0, 0, 0, 0, 1]
             ]

if __name__ == '__main__':
    print(solution(n, computers))
