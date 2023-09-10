#벨만포드 알고리즘에서 음수 사이클은 적당히 반복하면 되지만 양수 사이클은 많은 것을 반복해야 한다. 
import sys
input = sys.stdin.readline
n,start,end,m = map(int,input().split())
edges = []
distance = [-sys.maxsize]*n
for _ in range(m):
    start,end,value = map(int,input().split())
    edges.append((start,end,value))

citymoney = list(map(int,input().split()))

distance[start] = citymoney[start]
for i in range(n+101):
    for start,end,value in edges:
        if distance[start] == -sys.maxsize:
            continue
        elif distance[start] == sys.maxsize:
            distance[end] = sys.maxsize
        elif distance[end] < distance[start]+citymoney[end]-value:
            distance[end] = distance[start]+citymoney[end]-value
            if i>=n-1: #반복한 것이 n-1이 넘었는데도 값이 계속 증가한다면 양수 사이클이기 때문에 바꿔준다.
                distance[end] = sys.maxsize

if distance[end] == -sys.maxsize:
    print("gg")
elif distance[end] == sys.maxsize:
    print("Gee")
else:
    print(distance[end])