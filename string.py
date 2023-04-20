#백준 알고리즘 단계별로 풀기
#파이썬
#문자열
#27866
a=input()
b=int(input())
a=list(a)
print(a[b-1])
#2743
c=input()
c=list(c)
print(len(c))
#9086
d=int(input())
for _ in range(d):
    e=input()
    e=list(e)
    print(e[0],e[-1],sep='')
#11718
while True :
    try :
        f=input()
        print(f)
    except EOFError:
        break
