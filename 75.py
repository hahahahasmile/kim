#최소 공통 조상을 구하는 것은 bfs형식으로 찾는다. 깊이가 있어야 한다. 부모도 있어야 된다.
import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write
n = int(input())
visited=  [False]*(n+1)
tree = [[]for _ in range(n+1)]
depth = [0]*(n+1)
length = 1
treeheight = 0
while length<=n:
    length<<=1  #2의 배수승으로 곱하면 깊이를 구할 수 있다. 
    treeheight+=1

for _ in range(0,n-1):
    s,e =map(int,input().split())
    tree[s].append(e)
    tree[e].append(s)


parent = [[0 for j in range(n+1)] for i in range(treeheight+1)]

def bfs(node):
    visited[node] = True
    queue = deque()
    queue.append(node)
    level =1
    count =0
    now_size =1
    while queue:
        now = queue.popleft()
        for next in tree[now]:
            if not visited[next]:
                visited[next] =True
                parent[0][next] = now
                depth[next] = level
                queue.append(next)
        count+=1
        if count == now_size:
            count =0
            level+=1
            now_size = len(queue)

bfs(1)

for k in range(1,treeheight+1):
    for i in range(1,n+1):
        parent[k][n] = parent[k-1][parent[k-1][n]] # n번째 부모를 구할려면 이렇게 

def executelca(a,b):
    if depth[a] > depth[b]:
        temp =a
        a= b
        b = temp
    for k in range(treeheight,-1,-1):
        if pow(2,k) <= depth[b]-depth[a]: #2의 n승으로 해서 더 빠르게 구할 수 있도록
            if depth[a] <= depth[parent[k][b]]:
                b =parent[k][b]
    for k in range(treeheight,-1,-1):
        if a==b:break
        if parent[k][a] != parent[k][b]:
            a = parent[k][a]
            b = parent[k][b]
    lca =a
    if a!=b:
        lca = parent[0][lca]
    return lca

m =int(input())
for _ in range(m):
    a,b = map(int,input().split())
    print(str(executelca(a,b)))
    print("\n")