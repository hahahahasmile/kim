import sys
print = sys.stdout.write
A = list(input())
for i in range(len(A)):
    max = i
    for j in range(i+1,len(A)):
        if A[j]>A[max]:
            max=j
    if A[max]>A[i]:
        index = A[max]
        A[max] = A[i]
        A[i] = index

for i in range(len(A)):
    print(A[i])