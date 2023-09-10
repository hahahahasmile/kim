def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

a,b = map(int,input().split())
result = gcd(b,a)
while result>=1:
    print(1,end='') #1111 같은 형태로 만들고 싶을 때 end=''을 붙여준다.
    result-=1

