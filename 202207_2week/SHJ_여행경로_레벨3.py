'''
여행경로
'''

from collections import deque
import copy

def bfs(graph, start):
    visit = []
    
    queue = deque([start])
    while queue:
        cur =  queue.popleft()
        
        visit.append(cur)
        
        if cur not in graph:
            return visit
        elif len(graph[cur])==0:
            return visit
        
        queue.append(graph[cur].pop(0))
    return visit    # words 리스트에 target은 있으나 변환할 수 없는 경우


def dfs(graph, city, depth, count, visit):
    if depth == count:
            return True, visit

    if city in graph and len(graph[city])>0 :
        for c2 in graph[city]:
            g2 = copy.deepcopy(graph)
            g2[city].remove(c2)

            v2 = visit.copy()
            v2.append(c2)
            bResult, result = dfs(g2, c2, depth+1, count, v2)
            if bResult:
                return bResult, result
                
    return False, []
def solution(tickets):
    answer = 0
    start = 'ICN'
    graph = {}
    for t in tickets:
        key = t[0]
        value = t[1]
        if key in  graph:
            graph[key].append(value)
        else:
            graph[key] = []
            graph[key].append(value)
        
    for k, v in graph.items():
        graph[k] = sorted(v)
    # answer = bfs(graph, start)
    bResult, answer = dfs(graph, start, 0, len(tickets), [start])

    return answer


# tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
tickets = [["ICN", "A"], ["ICN", "B"], ["A", "ICN"]]
solution(tickets)

