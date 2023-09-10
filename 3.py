import sys
input = sys.stdin.readline
n,m=map(int,input().split())
numbers = list(map(int,input().split()))
psum = [0]
temp =0
for i in numbers:
    temp+=i
    psum.append(temp)
for i in range(m):
    s,e = map(int,input().split())
    result = psum[e]-psum[s-1]
    print(result)
    
