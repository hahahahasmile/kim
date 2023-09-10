#이 문제의 핵심은 연결되어 있는 리스트들을 모두 파악해야 된다는 것이다. 그러므로 시작하는 점들은 모두 다른 점에서 시작하게 하고 그 값들을 모두 저장해야 한다.
from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
A = [[] for _ in range(n+1)]
answer = [0]*(n+1)
def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v]= True
    while queue:
        now = queue.popleft()
        for i in A[now]:
            if not visited[i]:
                visited[i] = True
                answer[i]+=1
                queue.append(i)
for _ in range(m):
    s,e= map(int,input().split())
    A[s].append(e)

for i in range(1,n+1):
    visited = [False]*(n+1)
    bfs(i)
maxval =0
for i in range(1,n+1):
    maxval = max(maxval,answer[i])

for i in range(1,n+1):
    if maxval == answer[i]:
        print(i, end=' ')