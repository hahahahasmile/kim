#다익스트라 알고리즘은 연결된 부문에서 최단거리를 탐색하는 것 하나의 시작점에서부터 시작하는 것이기 때문에 위상 리스트하고는 틀리다.
import sys
input = sys.stdin.readline
from queue import PriorityQueue
n,m = map(int,input().split())
start =int(input())
A = [[] for _ in range(n+1)]
distance = [sys.maxsize]*(n+1)
visited = [False]*(n+1)
for i in range(m):
    s,e,v = map(int,input().split())
    A[s].append((e,v))

q= PriorityQueue() #연결된 노드들 중에서 숫자가 가장 작은 것부터 처리하기 위해서 우선순위 큐를 사용?
q.put((0,start))
distance[start] = 0
while q.qsize()>0: #우선순위 큐는 qsize()라고 명시한다.
    current = q.get()
    now = current[1]
    if visited[now]:
        continue
    visited[now] = True
    for tmp in A[now]:
        next =tmp[0]
        value= tmp[1]
        if distance[next]>distance[now]+value:
            distance[next] = distance[now]+value
            q.put((distance[next],next))

for i in range(1,n+1):
    if visited[i]:
        print(distance[i])
    else:
        print("INF")