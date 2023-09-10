n,m = map(int,input().split())
truep = list(map(int,input().split()))
T = truep[0]
del truep[0]
result =0
party = [[] for _ in range(m)]
def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]
def union(a,b):
    a = find(a)
    b = find(b)
    if a!=b:
        parent[b] = a
for i in range(m):
    party[i] = list(map(int,input().split()))
    del party[i][0]

parent = [0]*(n+1)
for i in range(n+1):
    parent[i] =i

for i in range(m):
    index = party[i][0]
    for j in range(1,len(party[i])):
        union(index,party[i][j])
for i in range(m):
    index = party[i][0]
    ischeck = True
    for j in range(T):
        if find(index) == find(truep[j]):
            ischeck =False
            break
    if ischeck:
        result+=1

print(result)
