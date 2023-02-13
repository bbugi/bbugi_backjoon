import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
# print(graph)
visited = [False] * (n+1)
# print(visited)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
# 갈 수 있는 수 중에 작은 수부터 진입해야 하므로 sort 해야함
for i in range(1, n+1):
    graph[i].sort()

# print(graph)
dfs_list = []
def dfs(graph, visited, visit_num):
    # 탐색 시작할 숫자부터 방문이 되니까 바로 visited에 
    visited[visit_num] = True
    # print(visit_num, end=" ")
    dfs_list.append(visit_num)

    # 그리고나서 탐색 시작한 숫자와 연결된 숫자들로 돌면서
    # 방문 확인하면서 탐색 마저하기
    for i in graph[visit_num]:
        if not visited[i]: # 방문한 적이 없다면
            dfs(graph, visited, i)

    return dfs_list
    

# bfs 
# dfs와 그래프는 동일한 모양임
from collections import deque

bfs_list = []
def bfs(graph, visited, visit_num):
    # 앞서 dfs에서 visited가 True로 채워져있기 때문에
    # 초기화 작업을 해줘야 함
    visited = [False] * (n+1)
    # 탐색할 숫자를 큐에 넣어주기
    queue = deque([visit_num])

    # 방문했다면 방문리스트를 True로 바꾸기
    visited[visit_num] = True

    while queue: # 큐가 비어있으면 False가 되면서 자동으로 while문이 멈춘다.
        # 큐에서 빠지는 숫자가 다음에 방문하는 숫자가 됨
        pop_v = queue.popleft()
        bfs_list.append(pop_v)

        for i in graph[pop_v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return bfs_list


print(*dfs(graph, visited, v))
print(*bfs(graph, visited, v))