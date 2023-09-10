import sys
n,m= map(int,input().split())
distance = [[sys.maxsize for j in range(n+1)] for i in range(n+1)]

for i in range(1,n+1):
    distance[i][i] =0

for i in range(m):
    start,end = map(int,input().split())
    distance[start][end] =1
    distance[end][start]=1

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if distance[i][j] > distance[i][k] + distance[k][j]:
                distance[i][j] = distance[i][k] + distance[k][j]

sum =sys.maxsize
index =0
for i in range(1,n+1):
    count =0
    for j in range(1,n+1):
        count += distance[i][j]
    if sum>count:
        sum = count
        index = i
print(index)
