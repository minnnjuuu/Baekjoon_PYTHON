#백준 알고리즘 단계별로 풀기
#파이썬
#반복문
#2739
n=int(input())
for x in range(1,10):
    print(n,'*',x,'=',n*x)
#10950
t=int(input())
for x in range (t):
    m,n=map(int,input().split())
    print(m+n)
#8393
n=int(input())
sigma=int(n*(n+1)*0.5)
print(sigma)
#25304
x=int(input())
n=int(input())
m=1
cnt=0
while m<=n:
    a,b=map(int,input().split(' '))
    cnt=cnt+a*b
    m=m+1
if cnt==x:
    print('Yes')
else:
    print('No')
#25314
a=int(input())
for x in range(a//4+1):
    if x == a//4:
        print("int")
    else :
        print("long ",end='')
#15552
import sys
t=int(input())
for x in range(t):
    m,n=map(int,sys.stdin.readline().split())
    print(m+n)
#11021
n=int(input())
for x in range(1,n+1):
    m,n=map(int,input().split())
    print('Case #',x,': ',m+n,sep='')
#11022
n=int(input())
for x in range(1,n+1):
    m,n=map(int,input().split())
    print('Case #',x,': ',m,' + ',n,' = ',m+n,sep='')
#2438
n=int(input())
for x in range(1,n+1):
    print(x*'*')
#2439
n=int(input())
for x in range(1,n+1):
    print(' '*(n-x)+'*'*x)
#10952
while True :
    m,n=map(int,input().split())
    if m==0 and n==0:
        break
    print(m+n)
#10951
while True :
    try:
        m,n=map(int,input().split())
        print(m+n)
    except:
        break