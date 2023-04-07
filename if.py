#백준 알고리즘 단계별로 풀기
#파이썬
#조건문
#1330
a,b=map(int,input().split())
if a>b :
    print('>')
elif a<b :
    print('<')
else:
    print('==')
#9498
score=int(input())
if score>=90 and score<=100:
    print('A')
elif score>=80 and score<=89:
    print('B')
elif score>=70 and score<=79:
    print('C')
elif score>=60 and score<=69:
    print('D')
else:
    print('F')
#2753
year=int(input())
if year%4==0 and year%100!=0:
    print('1')
elif year%400==0:
    print('1')
else :
    print('0')
#14681
x=int(input())
y=int(input())
if x>0 and y>0 :
    print('1')
elif x<0 and y>0 :
    print('2')
elif x<0 and y<0 :
    print('3')
elif x>0 and y<0 :
    print('4')
#2884
H,M=map(int,input().split())
if H==0 and M<45 :
    H=23
    M=M+15
    print(H,M)
elif M>=45 and M<=59:
    M=M-45
    print(H,M)
elif M>=0 and M<45:
    H=H-1
    M=M+15
    print(H,M)
#2525
A,B=map(int,input().split())
C=int(input())
if 60*A+B+C>=1440:
    D=60*A+B+C-1440
    H=D//60
    M=D%60
    print(H,M)
else :
    D=60*A+B+C
    H=D//60
    M=D%60
    print(H,M)
#2480
a,b,c=map(int,input().split())
money=0
if a==b and b==c :
    money=10000+1000*a
    print(money)
elif a!=b and b!=c and c!=a:
    max_abc=max(a,b,c)
    money=100*max_abc
    print(money)
elif a==b and a!=c:
    money=1000+100*a
    print(money)
elif b==c and a!=b:
    money=1000+100*b
    print(money)
elif a==c and a!=b:
    money=1000+100*a
    print(money)