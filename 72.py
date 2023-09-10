#a번째에서 b번쨰에서의 최소의 정수를 찾아라는 것은 세그먼트 트리를 이용하여서 풀 수 있다. 
import sys
input = sys.stdin.readline
n,m =map(int,input().split())
length = n
treeheight =0
while length != 0:
    length//=2
    treeheight+=1

treesize = pow(2,treeheight+1)
leftnodestartindex = treesize//2-1
tree = [sys.maxsize]*(treesize+1)

def partfind(s,e):
    result = sys.maxsize
    while s<=e:
        if s%2==1:
            result = min(result,tree[s])
            s+=1
        if e%2 ==0:
            result = min(result,tree[e])
            e-=1
        e = e//2
        s = s//2
    return result

def settree(index):
    while index!=1:
        if tree[index//2] > tree[index]:
            tree[index//2] = tree[index]
        index-=1

for i in range(leftnodestartindex+1, leftnodestartindex+n+1):
    tree[i] = int(input())

settree(treesize-1)

for _ in range(m):
    s,e = map(int,input().split())
    s = leftnodestartindex+s
    e = leftnodestartindex+e
    print(partfind(s,e))
