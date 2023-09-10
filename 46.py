from collections import deque
import sys
input = sys.stdin.readline
n,m,k,x = map(int,input().split())
# 처음 시작하는 도시에서 각 도시들의 거리를 재는 것이므로 bfs를 하는 것이 적합하다고 판단된다.
A = [[] for _ in range(n+1)]
visited = [-1]*(n+1)
answer = []
def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] +=1
    while queue:
        now = queue.popleft()
        for i in A[now]:
            if visited[i]==-1:
                visited[i] =visited[now]+1
                queue.append(i)
for _ in range(m):
    s,e = map(int,input().split())
    A[s].append(e)

bfs(x)
for i in range(1,n+1):
    if visited[i] ==k:
        answer.append(i)

if not answer:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)