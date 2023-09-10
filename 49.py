#물통이 3개 있다. 3차원 배열을 만들려면 초과가 됨으로 2차원 배열을 만든다. 두 개의 물병을 알면 나머지  한개는 파악할 수 있다. 
from collections import deque
sender = [0,0,1,1,2,2]
receiver = [1,2,0,2,0,1]
now = list(map(int,input().split()))
visited =[[False for j in range(201)] for i in range(201)]
answer= [False]*(201)
def bfs():
    queue = deque()
    queue.append((0,0))
    visited[0][0] = True
    answer[now[2]] = True
    while queue:
        node = queue.popleft()
        a = node[0]
        b = node[1]
        c = now[2]-a-b
        for k in range(6):
            next = [a,b,c]
            next[receiver[k]]+=next[sender[k]]
            next[sender[k]] =0
            if next[receiver[k]]> now[receiver[k]]:
                next[sender[k]] = next[receiver[k]] -now[receiver[k]]
                next[receiver[k]] = now[receiver[k]]
            if not visited[next[0]][next[1]]:
                visited[next[0]][next[1]] = True
                queue.append((next[0],next[1]))
                if next[0] ==0:
                    answer[next[2]] = True
bfs()
for i in range(len(answer)):
    if answer[i]:
        print(i, end =' ')