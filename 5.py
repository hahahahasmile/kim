import sys
input = sys.stdin.readline
n,m = map(int,input().split())

A = list(map(int,input().split()))
D = [0]*n # 합 배열 만들기
C = [0]*m # 나머지 배열 만들기
D[0] = A[0]
answer =0
for i in range(1,n):
    D[i] = D[i-1]+A[i]

for i in range(n):
    temp = D[i]%m
    if temp == 0:
        answer+=1
    C[temp]+=1
print(answer)
for i in range(m):
    if C[i]>1:
        answer+=(C[i] *(C[i]-1) // 2)

print(answer)