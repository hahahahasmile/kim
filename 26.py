from collections import deque # 큐를 사용하기 위해서는 deque을 사용한다. 파이썬에서는
n,m,start = map(int,input().split())
A = [[] for _ in range(n+1)]
for _ in range(m):
    s,e = map(int,input().split())
    A[s].append(e)
    A[e].append(s)
for i in range(1,n+1):
    A[i].sort()
def dfs(v):
    print(v, end = ' ')
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            dfs(i)

visited = [False]*(n+1)
dfs(start)

def bfs(v):
    queue = deque()
    queue.append(v) # 큐에 수를 집어넣는 것
    visited[v] = True
    while queue:
        now = queue.popleft() #큐의 마지막을 꺼내는 것 
        print(now,end=' ')
        for i in A[now]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
print()
visited = [False]*(n+1)
bfs(start)