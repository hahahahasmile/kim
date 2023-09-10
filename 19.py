# n 번째 수를  구한다는 것은 피벗정렬을 이용한다는 것 피벗 정렬은 피벗을 찾는 함수와 정렬을 하는 함수 크게 2가지로 이루어져있다. 
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
A = list(map(int,input().split()))
def quicksort(s,e,k): #피벗을 찾는 함수이다. 피벗과 k번째 수의 대소관계를 비교해서 수색해야 될 곳을 물색하는 함수이다.
    global A 
    if s<e:
        pivot = find(s,e)
        if pivot ==k:
            return
        elif pivot<k:
            quicksort(pivot+1,e,k)
        else:
            quicksort(s,pivot-1,k)
    
def swap(i,j):
    global A
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
def find(s,e):
    global A
    if s+1==e: #시작과 끝이 한 개차이가 나면 대소관계만 비교해서 swap
        if A[s]>A[e]:
            swap(s,e)
        return e
    
    m = (s+e)//2 
    swap(s,m)
    pivot = A[s] #피벗을 시작과 끝의 중간지점의 수로 정한다. 중간 지점의 수를 맨 앞으로 끌고 오니까 시작점은 원래 시작점의 +1 이고 끝점은 그대로이다.
    i = s+1
    j = e
    while i<=j:
        while pivot <A[j] and j>0:  #끝 수는 피벗의 수보다 작은 수가 나올 때까지 계속
            j= j-1
        while pivot >A[i] and i<len(A)-1:  #시작 수는 피벗의 수보다 큰 수가 나을 때까지 계속
            i = i+1
        if i<=j:  #꿑점을 중심으로 작업한다. 이런 류의 작업들은
            swap(i,j)
            i = i+1
            j = j-1
    A[s] = A[j]   # 원래 피벗이 있어야 하는 위치인 j로 보내준다.
    A[j] = pivot
    return j
quicksort(0,n-1,m-1)
print(A[m-1])

