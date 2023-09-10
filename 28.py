from collections import deque
n= int(input())
A = [[] for _ in range(n+1)]
for i in range(1,n+1):
    data = list(map(int,input().split()))
    index=0
    s= data[index]
    index+=1
    while True:
        e= data[index]
        if e==-1:
            break
        v = data[index+1]
        A[s].append((e,v))
        index+=2

def bfs(v):
    queue = deque()
    visited[v] = True
    queue.append(v)
    while queue:
        now = queue.popleft()
        for i in A[now]:
            next = i[0]
            if not visited[i[0]]:
                visited[i[0]] = True
                queue.append(i[0])
                distance[i[0]] = distance[now]+i[1]

visited = [False]*(n+1)
distance = [0]*(n+1)
bfs(1)
max =1
for i in range(2,n+1):
    if distance[i]>distance[max]:
        max = i

distance = [0]*(n+1)
visited = [False]*(n+1)
bfs(max)
distance.sort()
print(distance[n])