n,m = map(int,input().split())
parent = [0]*(n+1)
for i in range(0,n+1):
    parent[i] = i

def find(a):
    if a==parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]
def union(a,b):
    a1 = find(a)
    b1 = find(b)
    if a1!=b1:
        parent[b1] = a1

for _ in range(m):
    v,s,e = map(int,input().split())
    if v==0:
        union(s,e)
    else:
        if parent[s] == parent[e]:
            print("YES")
        else:
            print("NO")