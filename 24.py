import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
n = int(input())
def isprime(num):
    for i in range(2,int(num/2+1)):
        if num%i ==0:
            return False
    return True
def dfs(num, index):
    global n
    if index == n:
        print(num)
    else:
        for i in range(1,10):
            if i%2 ==0:
                continue
            else:
                if isprime(num*10+i):
                    dfs(num*10+i,index+1)

dfs(2,1)
dfs(3,1)
dfs(5,1)
dfs(7,1)
