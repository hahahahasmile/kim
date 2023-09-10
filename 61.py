import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
distance = [[sys.maxsize for j in range(n+1)] for i in range(n+1)]
for i in range(n+1):
    distance[i][i] = 0
for i in range(m):
    start,end,value = map(int,input().split())
    if distance[start][end]>value:
        distance[start][end] = value

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if distance[i][j] > distance[i][k]+distance[k][j]:
                distance[i][j] = distance[i][k]+distance[k][j]

for i in range(n+1):
    for j in range(n+1):
        if distance[i][j] == sys.maxsize:
            print(0,end= ' ')
        else:
            print(distance[i][j], end = '')
    print()