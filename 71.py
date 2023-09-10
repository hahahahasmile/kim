import sys
input = sys.stdin.readline
n,m,k = map(int,input().split())
treeheight = 0 # 트리의 높이
length = n # 리프노드의 개수 
while length!=0:
    length //=2
    treeheight+=1 # length 를 /2를 하면서 트리의 높이를 더한다. 

treesize = pow(2,treeheight+1) #트리의 크기는 2의 트리의 높이승이다. 
leftnodestartindex = treesize//2-1 # 처음에 인수들을 집어넣는 것들은 treesize//2한 곳에서 -1을 한것
tree = [0]*(treesize+1)

for i in range(leftnodestartindex+1,leftnodestartindex+n+1):
    tree[i] = int(input())

def settree(i):
    while i!= 1:
        tree[i//2] +=tree[i]
        i-=1
def changeval(index,value):
    diff = value - tree[index]
    while index>0:
        tree[index] = tree[index]+diff
        index = index//2 #위에 있는 값들도 바뀌기 때문에
def getsum(s,e):
    partsum =0
    while s<=e:
        if s%2 ==1:
            partsum+=tree[s]
            s+=1
        if e%2==0:
            partsum += tree[e]
            e-=1
        s = s//2
        e = e//2
    return partsum

settree(treesize-1)

for i in range(m+k):
    question,s,e= map(int,input().split())
    if question ==1:
        changeval(leftnodestartindex+s,e)
    elif question ==2:
        s = s+leftnodestartindex
        e = e+leftnodestartindex
        print(getsum(s,e))