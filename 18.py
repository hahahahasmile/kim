n = int(input())
A = list(map(int,input().split()))
S = [0] *n
B = sorted(A)
S[0] = B[0]
for i in range(1,n):
    S[i] = S[i-1]+B[i]
sum = 0
for i in range(0,n):
    sum+=S[i]

print(sum)