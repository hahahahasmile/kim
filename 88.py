#마지막으로 끝나는 수가 문제해결의 키가 되는 문제일 떄는 배열에 그것을 표현해 줘야 한다. 
import sys
input = sys.stdin.readline
n = int(input())
D = [[0 for j in range(10)] for i in range(n+1)]

mod = 1000000000
for i in range(1,10):
    D[1][i] =1

for i in range(2,n+1):
    for j in range(0,10):
        if j==0:
            D[i][j] =(D[i-1][j+1])%mod
        elif j==9:
            D[i][j] = (D[i-1][j-1])%mod
        else:
            D[i][j] = (D[i-1][j-1]+D[i-1][j+1])%mod

sum = 0
for i in range(10):
    sum = (sum+D[n][i])%mod

print(sum)