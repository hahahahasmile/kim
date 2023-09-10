from collections import deque
n = int(input())
A= [[] for _ in range(n+1)]
B= [0]*(n+1)
indegree= [0]*(n+1)
C = [0]*(n+1)
for i in range(1,n+1):
    inputlist =list(map(int,input().split()))
    B[i] = (inputlist[0])
    index=1
    while True:
        pretemp = inputlist[index]
        if pretemp == -1:
            break
        index+=1
        A[pretemp].append(i)
        indegree[i]+=1

queue = deque()
for i in range(1,n+1):
    if indegree[i]==0:
        queue.append(i)

while queue:
    now = queue.popleft()
    for next in A[now]:
        indegree[next]-=1
        C[next] = max(C[next], C[now]+B[now])
        if indegree[next]==0:
            queue.append(next)

for i in range(1,n+1):
    print(B[i]+C[i])