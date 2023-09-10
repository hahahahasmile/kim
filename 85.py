import sys
input = sys.stdin.readline
n = int(input())
D = [0]*(n+1)
T = [0]*(n+1)
P = [0]*(n+2)
for i in range(1,n+1):
    t,v = map(int,input().split())
    T[i] = t
    D[i] = v

for i in range(n,0,-1):
    if i+T[i]>n+1:
        P[i] = P[i+1]
    else:
        P[i] = max(P[i+1],D[i]+P[i+T[i]])

print(P[i+1])
