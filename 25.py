import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
n,m = map(int,input().split())
A = [[] for _ in range(n)]
visited = [False]*n
answer= False
def dfs(v, depth):
    global answer
    if depth ==5:
        answer = True
        return
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            dfs(v,depth+1)
    visited[v] = False
for _ in range(m):
    s,e = map(int,input().split())
    A[s].append(e)
    A[e].append(s)

for i in range(n):
    dfs(i,1)
    if answer:
        break

if answer:
    print(1)
else:
    print(0)