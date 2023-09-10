import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write
n = int(input())
tree = [[]for _ in range(n+1)]

for _ in range(0,n-1):
    s,e = map(int,input().split())
    tree[s].append(e)
    tree[e].append(s)

depth = [0]*(n+1) # 최소 공통 조상을 찾는 것이기 때문에 깊이 노드를 구해야하는 것이다. 
parent = [0]*(n+1)
visited = [False]*(n+1)

def bfs(node):
    queue = deque()
    queue.append(node)
    visited[node] = True
    level =1
    now_size =1
    count =0
    while queue:
        now = queue.popleft()
        for next in tree[now]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)
                parent[next] = now
                depth[next] = level
        count+=1
        if count == now_size: #now_size 는 부모 노드가 포함하고 있는 자식노드인 것이다. 그래서 bfs로 문제를 푸는 것이다. 
            count =0
            now_size = len(queue)
            level+=1

bfs(1)

def executelca(a,b):
    if depth[a] < depth[b]:
        temp =a
        a = b
        b= temp
    while depth[a]!= depth[b]:
        a = parent[a]
    
    while a!=b:
        a = parent[a]
        b = parent[b]
    
    return a
m = int(input())
for _ in range(m):
    a,b= map(int,input().split())
    print(str(executelca(a,b)))
    print("\n")
