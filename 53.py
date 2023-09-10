#크기를 비교해서 순서대로 줄을 세운다. 위상정렬
from collections import deque
n,m = map(int,input().split())
A = [[] for _ in range(n+1)]
D = [0]*(n+1)
for i in range(m):
    s,e = map(int,input().split())
    A[s].append(e)
    D[e]+=1

queue = deque()
for i in range(1,n+1):
    if D[i] ==0:
        queue.append(i)

while queue:
    now = queue.popleft()
    print(now, end = ' ')
    for i in A[now]:
        D[i]-=1
        if D[i] ==0:
            queue.append(i)
        

