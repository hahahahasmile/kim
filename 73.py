import sys
input =sys.stdin.readline
n,m,k = map(int,input().split())
length =n
treeheight = 0
mod = 1000000007
while length !=0:
    length //=2
    treeheight+=1

treesize = int(pow(2,treeheight+1))
leftnodestartindex = treesize//2-1
tree = [1]*(treesize+1)
for i in range(leftnodestartindex+1, leftnodestartindex+1+n):
    tree[i] = int(input())

def settree(index):
    while index!=1:
        tree[index//2] = tree[index//2]*tree[index] %mod
        index-=1

def changeval(index,value):
    tree[index] = value
    while index>1:
        index = index//2
        tree[index] = tree[index*2]*tree[index*2+1] %mod

def printsum(s,e):
    result =1
    while(s<=e):
        if s%2==1:
            result = result * tree[s]%mod
            s+=1
        if e%2==0:
            result = result * tree[e]%mod
            e-=1
        s = s//2
        e = e//2
    return result

settree(treesize-1)
for i in range(m+k):
    question,s,e = map(int,input().split())
    if question ==1:
        changeval(leftnodestartindex+s,e)
    elif question ==2:
        s = s+leftnodestartindex
        e = e+leftnodestartindex
        print(printsum(s,e))