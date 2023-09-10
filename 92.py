#왼쪽 오른쪽에 보이는 빌딩 수가 달라질때 가장 큰 빌딩부터 먼저 세운다고 가정한다.
import sys
input = sys.stdin.readline
n,l,r = map(int,input().split())
D = [[[0 for k in range(101)]for j in range(101)] for i in range(101)]
D[1][1][1]=1
mod = 1000000007
for i in range(2,n+1):
    for j in range(1,l+1):
        for k in range(1,r+1):
            D[i][j][k] = (D[i-1][j][k] *(i-2) + (D[i-1][j-1][k]+D[i-1][j][k-1]))%mod

print(D[n][l][r])