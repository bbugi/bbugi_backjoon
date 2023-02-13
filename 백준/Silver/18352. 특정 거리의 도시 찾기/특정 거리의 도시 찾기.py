from collections import deque
import sys

input = sys.stdin.readline


n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
# print(graph)
visited = [-1] * (n+1)
# print(visited)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    # graph[b].append(a) # 양방향 그래프일때나 사용..

# print(graph)

def bfs(start_num):
    queue = deque([start_num])
    visited[start_num] = 0

    while queue:
        pop_num = queue.popleft()
        
        for i in graph[pop_num]:
            if visited[i] == -1:
                queue.append(i)
                visited[i] = visited[pop_num]+1

    return visited

# print(bfs(x))

if k not in bfs(x):
    print(-1)

# 출력시 오름차순으로 출력하라는 조건이 존재

else:
    ans = []
    for i in range(len(bfs(x))):
        # print(i)
        # print(bfs(x))
        # print(bfs(x)[i])
        if bfs(x)[i] == k:
            ans.append(i)

    print(*sorted(ans), sep='\n')