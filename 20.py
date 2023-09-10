#mergesort는 start end 라는 변수가 필요하다. 기존 변수들을 집어넣는 배열에서 정렬하는 배열을 만든 뒤 인덱스의 처음과 중간에서 시작해서 각각 비교하는 것이다.
import sys
input = sys.stdin.readline
print = sys.stdout.write
def merge(s,e):
    if e-s<1:return
    m = int(s+(e-s)/2)
    merge(s,m)
    merge(m+1,e)
    for i in range(s,e+1):
        tmp[i] = A[i]
    k = s
    index1 = s
    index2 = m+1
    while index1<=m and index2 <=e:
        if tmp[index1]>tmp[index2]:
            A[k] = tmp[index2]
            index2+=1
            k+=1
        else:
            A[k] = tmp[index1]
            index1+=1
            k+=1
    while index1<=m:
        A[k] = tmp[index1]
        index1+=1
        k+=1
    while index2<=e:
        A[k] = tmp[index2]
        index2+=1
        k+=1
    
n = int(input())
A = [0]*int(n+1)
tmp = [0]*int(n+1)
for i in range(1,n+1):
    A[i] = int(input())
merge(1,n)
for i in range(1,n+1):
    print(str(A[i])+'\n')