#mst ==  최소 신장 트리 최소 신장 트리는 다른 부모끼리 연결해야 한다. 가중치들이 최소가 되도록 가중치를 기점으로 정렬한다.
import sys
from queue import PriorityQueue
input = sys.stdin.readline
n,m = map(int,input().split())
pq = PriorityQueue()
parent = [0]*(n+1)
for i in range(n+1):
    parent[i] = i

for i in range(m):
    s,e,v = map(int,input().split())
    pq.put((v,s,e))

def find(a):
    if a ==parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)
    if a!=b:
        parent[b] =a

useedge =0
result =0

while useedge<n-1: # 최소 신장트리는 n-1개의 에지를 사용한다. 
    v,s,e = pq.get()
    if find(s)!= find(e):
        union(s,e)
        useedge+=1
        result+=v

print(result)