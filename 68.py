import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
visited = [False]*(n)
tree = [[] for _ in range(n)]
p = list(map(int,input().split()))
answer = 0
for i in range(n):
    if p[i] !=-1:
        tree[i].append(p[i])
        tree[p[i]].append(i)
    else:
        root = i

def dfs(number):
    global answer #answer 전역 변수
    visited[number] = True
    count =0
    for next in tree[number]:
        if not visited[next] and next!= deletenode:
            count+=1
            dfs(next)
    if count ==0:
       answer+=1
deletenode  =int(input())
if deletenode ==root:
    print(0)
else:
    dfs(root)
    print(answer)