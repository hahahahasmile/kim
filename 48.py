#이분 그래프의 판별은 방문한  노드가 연결된 바로 그전의 노드와 숫자가  같으면 이분 그래프가 아닌 것이다.
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
isEven = True
def dfs(node):
    visited[node] = True
    for i in A[node]:
        global isEven
        if not visited[i]:
            checked[i] = (checked[node]%2)+1
        elif checked[node] == checked[i]:
            isEven =False

for _ in range(n):
    v,e = map(int,input().split())
    A = [[] for _ in range(v+1)]
    checked = [0]*(v+1)
    visited = [False]*(v+1)
    isEven = True
    for i in range(e):
        s,e = map(int,input().split())
        A[s].append(e)
        A[e].append(s)
    for i in range(1,v+1):
        if isEven:
            dfs(i)
        else:
            break
    if isEven:
        print("YES")
    else:
        print("NO")