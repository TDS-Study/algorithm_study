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
    
    # 더 갈곳이 없다
    if start not in graph.keys() or len(graph[start]) == 0:
        if len(visited) == end_count:
            return visited
        else:
            return None

    next_city = graph[start].pop(0)
    visited.append(next_city)
    
    return dfs(graph, next_city, visited, end_count)

def solution(tickets):
    answer = []
    graph = {}
    
    # 출발도시, 도착도시로 된 딕셔너리 생성
    # 일방통행 이므로 도착도사, 출발도시는 생성 안함
    # 표를 다 써야하므로 중복 허용, set 쓰면 안됨
    for i in range(len(tickets)):
        if tickets[i][0] not in graph:
            graph[tickets[i][0]] = []

        graph[tickets[i][0]].append(tickets[i][1])
        
    for i in graph.values():
        i.sort()

    answer.append("ICN")
    answer = dfs(graph, "ICN", answer, len(tickets)+1)

    return answer

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]

if __name__ == "__main__":

    print(solution(tickets))