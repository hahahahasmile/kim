#최장 공통 부분 수열 찾는 것은 두 문자열을 비교하는 것 -> 같으면 대각선의 값 다르면 왼쪽과 위쪽의 값 중 큰 것 그 값들로 기록을 더듬어 간다. 
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
A= list(input())
A.pop() # \n 문자열 없애기
B = list(input())
B.pop()
D = [[0 for j in range(len(B)+1)] for i in range(len(A)+1)]
Path = []
for i in range(1,len(A)+1):
    for j in range(1,len(B)+1):
        if A[i-1] == B[j-1]:
            D[i][j] = D[i-1][j-1]+1
        else:
            D[i][j] = max(D[i-1][j],D[i][j-1])

print(D[len(A)][len(B)])

def gettext(r,c):
    if r==0 or c==0:
        return
    if A[r-1] == B[c-1]:
        Path.append(A[r-1])
        gettext(r-1,c-1)
    else:
        if D[r-1][c]>D[r][c-1]:
            gettext(r-1,c)
        else:
            gettext(r,c-1)

gettext(len(A),len(B))
for i in range(len(Path)-1,-1,-1):
    print(Path.pop(i),end =' ')

print()