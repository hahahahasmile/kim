result =0
def merge(s,e):
    global result
    if e-s<1: return
    m = int(s+(e-s)/2)
    merge(s,m)
    merge(m+1,e)
    for i in range(s,e+1):
        tmp[i] = A[i]
    k = s
    index1 = s
    index2 = m+1
    while index1<=m and index2<=e:
        if tmp[index1]>tmp[index2]:
            A[k] = tmp[index2]
            result = result+index2-k
            k+=1
            index2+=1
        else:
            A[k] = tmp[index1]
            k+=1
            index1+=1
    while index1<=m:
        A[k] = tmp[index1]
        k+=1
        index1+=1
    while index2<=e:
        A[k] = tmp[index2]
        k+=1
        index2+=1
n = int(input())
A = list(map(int,input().split()))
A.insert(0,0) #0을 첫 번째에 넣는다라는 뜻 
tmp = [0]*int(n+1)
merge(1,n)
print(result)