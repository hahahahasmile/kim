#트리 노드의 부모 찾기는 한 방향으로 계속 파는 dfs탐색을 이용해서 풀면 된다. 부모 자식 간에 연결되어 있으므로 자식은 연결된 부모를 parent에 저장하면 된다. 
n = int(input())
tree = [[]for _ in range(n+1)]
visited= [False] *(n+1)
answer = [0]*(n+1)
for i in range(n-1):
    s,e = map(int,input().split())
    tree[s].append(e)
    tree[e].append(s)

def dfs(number):
    visited[number ] =True
    for next in tree[number]:
        if not visited[next]:
            answer[next] = number
            dfs(next)

dfs(1)
for i in range(2,n+1):
    print(answer[i])