import sys
input = sys.stdin.readline
n = int(input())
D = [[0 for j in range(31)] for i in range(31)]

for i in range(0,31):
    D[i][0]= 1
    D[i][1] = i
    D[i][i] = 1

for i in range(2,31):
    for j in range(2,i):
        D[i][j] = D[i-1][j] + D[i-1][j-1]

for i in range(n):
    s,e= map(int,input().split())
    print(D[e][s])