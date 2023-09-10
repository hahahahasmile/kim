import sys
input = sys.stdin.readline
n,m = map(int,input().split())
DP = [[0 for j in range(1001)] for i in range(1001)]
max =0
for i in range(n):
    numbers = list(input())
    for j in range(m):
        DP[i][j] = int(numbers[j])
        if(DP[i][j] ==1 and i>0 and j>0):
            DP[i][j] = min(DP[i-1][j-1],DP[i-1][j],DP[i][j-1])+DP[i][j]
        if max<DP[i][j]:
            max = DP[i][j]

print(max*max)