from collections import deque

def bfs(graph, visit,root):
    queue = deque([root])
    while queue:
        n = queue.popleft()
        if n not in visit:
            visit.append(n)
            if n in graph:
                for n1 in graph[n]:
                    if n1 in visit:
                        continue
                    queue.append(n1)


def solution(n, computers):
    answer = 0
    graph = {}
    nList = [i for i in range(n)]
    
    for i in range(n):
        for j in range(1,n):
            # 자기 자신은 패스
            if i == j:
                continue
                
            #graph에 구성
            if computers[i][j] == 1:
                if i not in graph:
                    graph[i] = {j}
                else:
                    graph[i].add(j)
                
                if j not in graph:
                    graph[j] = {i}
                else:
                    graph[j].add(i)

    while len(nList) > 0:
        visit = []
        bfs(graph, visit, nList[0])
        nList = [x for x in nList if x not in visit]
        answer += 1
        
    return answer




n=3
computers = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
solution(n, computers)