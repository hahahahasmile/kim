n,m = map(int,input().split())
data = [0]*n
for i in range(n):
    data[i] = int(input())

count =0
for i in range(n-1,-1,-1):
    if data[i]<=m:
        count += m/data[i]
        m = m%data[i]

print(count)