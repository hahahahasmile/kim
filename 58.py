import sys
import heapq
input = sys.stdin.readline
n,m,k = map(int,input().split())
w = [[] for _ in range(n+1)]
distance = [[sys.maxsize] *k for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    w[a].append((b,c))
pq = [[0,1]]
distance[1][0] = 0
while pq:
    cost,node = heapq.heappop(pq)
    for nnode,ncost in w[node]:
        scost = cost+ncost
        if distance[nnode][k-1]>scost:
            distance[nnode][k-1] = scost
            distance[nnode].sort()
            heapq.heappush(pq,[scost,nnode])

for i in range(1,n+1):
    if distance[i][k-1] == sys.maxsize:
        print(-1)
    else:
        print(distance[i][k-1])