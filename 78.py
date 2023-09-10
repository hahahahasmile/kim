import sys
input = sys.stdin.readline
n = int(input())
D = [[0 for j in range(15)] for i in range(15)]

for i in range(1,15):
    D[i][1]=1
    D[0][i] = i

for i in range(1,15):
    for j in range(2,15):
        D[i][j] = D[i-1][j]+D[i][j-1] #점화식은 이렇게 도출된다. 

for i in range(n):
    s = int(input())
    e = int(input())
    print(D[s][e])