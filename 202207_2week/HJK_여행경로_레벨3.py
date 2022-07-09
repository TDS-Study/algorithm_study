"""문제 설명
주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 항상 "ICN" 공항에서 출발합니다.

항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한사항
모든 공항은 알파벳 대문자 3글자로 이루어집니다.
주어진 공항 수는 3개 이상 10,000개 이하입니다.
tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
주어진 항공권은 모두 사용해야 합니다.
만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
모든 도시를 방문할 수 없는 경우는 주어지지 않습니다."""
# https://school.programmers.co.kr/learn/courses/30/lessons/43164

def dfs(graph, start, visited, end_count):

    for i in graph[start]:
        # 안쓴 티켓 이라면 쓴다
        if i not in visited:
            next_city = i[2]
            # 참조하지 못하도록 copy 해서 새 list 생성
            new_visited = visited.copy()
            new_visited.append(i)
            v = dfs(graph, next_city, new_visited, end_count)

            if v != None:
                return v

    # 티켓을 다썼다
    if len(visited) == end_count:
        return visited
    else:
        return None

def solution(tickets):
    answer = []
    visited = []
    graph = {}
    
    # 출발도시, 도착도시로 된 딕셔너리 생성
    # 일방통행 이므로 도착도시, 출발도시 역순은 생성 안함
    for i in range(len(tickets)):
        # 출발 지를 딕셔너리 키에 추가
        if tickets[i][0] not in graph:
            graph[tickets[i][0]] = []
        # 도착 지를 딕셔너리 키에 추가
        if tickets[i][1] not in graph:
            graph[tickets[i][1]] = []
        
        # 표가 중복될 수 도 있을것 같아 순번 i 도 각 노드에 추가함
        l = [i]
        l.extend(tickets[i])
        graph[tickets[i][0]].append(l)
    
    # 각 노드가 가지고 있는 두번 째 (도착지) 기준으로 정렬
    for i in graph.values():
        i.sort(key= lambda x: x[2])

    visited = dfs(graph, "ICN", answer, len(tickets))

    # 도착지 공항을 answer에 추가하고 가장 앞에 ICN 추가
    answer = [_[2] for _ in visited]
    answer.insert(0, "ICN")

    return answer

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"],['SFO','ICN'],['ICN','SFO']]
tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
tickets = [['ICN','SFO'], ['ICN','XAB'], ['XAB','ICN']]

if __name__ == "__main__":

    print(solution(tickets))