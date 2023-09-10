from collections import deque
dx = [-1,0,1,0]
dy = [0,-1,0,1]
n,m = map(int,input().split())
A = [[0]*m for _ in range(n)] # 이차원 배열을 만들때 처음이 행을 나타내는 것 두 번째가 열을  나타내는 것
visited = [[False] *m for _ in range(n)]
def bfs(i,j):
    queue= deque()
    queue.append((i,j))
    visited[i][j] = True
    while queue:
        now = queue.popleft()
        for k in range(4):
            x = now[0]+dx[k]
            y = now[1]+dy[k]
            if x>=0 and y>=0 and x<n and y<m:
                if A[x][y]!=0 and not visited[x][y]:
                    visited[x][y] = True
                    A[x][y] = A[now[0]][now[1]]+1
                    queue.append((x,y))

for i in range(n):
    numbers= list(input())
    for j in range(m):
        A[i][j] = int(numbers[j])

bfs(0,0)
print(A[n-1][m-1])