n = int(input())
A = list(map(int,input().split()))
A.sort()
m = int(input())
targetlist = list(map(int,input().split()))
for i in range(m):
    find = False
    target = targetlist[i]
    start = 0
    end = len(A)-1
    while start<=end:
        mid = int((start+end)/2)
        midv = A[mid]
        if midv <target:
            start= mid+1
        elif midv>target:
            end = mid-1
        else:
            find = True
            break
    if find:
        print(1)
    else:
        print(0)