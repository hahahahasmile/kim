#시작점을 정한다. 그리고 그 지점에서 도착지점이 정해져있다. 그걸 구하기 위해서는 다익스트라 알고리즘
from queue import PriorityQueue
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
A= [[] for _ in range(n+1)]
distance = [sys.maxsize]*(n+1)
visited = [False]*(n+1)
for _ in range(m):
    s,e,v = map(int,input().split())
    A[s].append((e,v))

queue = PriorityQueue()
start,end =map(int,input().split())
distance[start] = 0
queue.put((0,start))
while queue.qsize()>0:
    current = queue.get()
    cv = current[1]
    if visited[cv]:
        continue
    visited[cv] = True
    for i in A[cv]:
        next = i[0]
        value = i[1]
        if distance[next]> distance[cv]+value:
            distance[next] = distance[cv]+value
            queue.put((distance[next],next))

if(visited[end]):
    print(distance[end])