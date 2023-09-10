#확률은 조합을 이용하여서 문제를 푼다.
D = [0]*51
p = [0]*51
n = int(input())
D = list(map(int,input().split()))
index = int(input())
T= 0
for i in range(n):
    T+=D[i]
ans =0
for i in range(n):
    if D[i]>=index:
        p[i]=1
        for k in range(0,index):
            p[i] = p[i] * (D[i]-k)/(T-k)
        ans+=p[i]

print(ans)