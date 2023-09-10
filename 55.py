#연결된 것들을 방문해야되는 것은 위상정렬 위상정렬을 할려면 연결되어 있는 곳을 카운트 해줘야 한다. 
from collections import deque
n = int(input())
m = int(input())
A = [[] for _ in range(n+1)]
reverseA = [[] for _ in range(n+1)]
index = [0]*(n+1)
result = [0]*(n+1)
for i in range(m):
    s,e,v = map(int,input().split())
    A[s].append((e,v))
    reverseA[e].append((s,v))
    index[e]+=1

start,end = map(int,input().split())
queue = deque()
queue.append(start)
while queue:
    now = queue.popleft()
    for next in A[now]:
        index[next[0]]-=1
        result[next[0]] = max(result[next[0]],result[now]+next[1])
        if index[next[0]] ==0:
            queue.append(next[0])

queue.clear()
queue.append(end)
visited = [False]*(n+1)
visited[end] = True
resultcount =0
while queue:
    now = queue.popleft()
    for next in reverseA[now]:
        if result[now] == result[next[0]]+next[1]:
            resultcount+=1
        if not visited[next[0]]:
            queue.append(next[0])

print(result[end])
print(resultcount)
