#백준 알고리즘 단계별로 풀기
#파이썬
#입출력과 사칙연산
#10807
n=int(input())
n_list=list(input().split())
n_num=str(input())
n_count=n_list.count(n_num)
print(n_count)
#10871
n,x=map(int,input().split())
a=list(map(int,input().split()))
for m in range (n):
    if a[m]<x:
        print(a[m],end=' ')
#10818
n=int(input())
a=list(map(int,input().split()))
min_a=min(a)
max_a=max(a)
print(min_a,max_a)
#2562
list_a=[]
for x in range(9):
    list_a.append(int(input()))
print(max(list_a))
print(list_a.index(max(list_a))+1)
#10810
n,m=map(int,input().split())
n_list=[0]*n
for _ in range (m):
    a,b,c=map(int,input().split())
    for x in range(a-1,b):
        n_list[x]=c
for x in n_list:
    print(x,end=' ')
#10813
n,m=map(int,input().split())
n_list=list(range(1,n+1))
for _ in range (m):
    a,b=map(int,input().split())
    c=0
    c=n_list[a-1]
    n_list[a-1]=n_list[b-1]
    n_list[b-1]=c
for x in n_list:
    print(x, end=' ')
#5597
num_list=list(range(1,31))
for x in range(28):
    n=int(input())
    num_list.remove(n)
print(num_list[0])
print(num_list[1])
#3052
list_10=[]
for x in range(10):
    list_10.append(int(input())%42)
list_set=set(list_10)
list_set_list=list(list_set)
print(len(list_set_list))
#10811
n,m=map(int,input().split())
n_list=list(range(1,n+1))
for _ in range(m):
    a,b=map(int,input().split())
    reverse_list=[0]*(b-a+1)
    for x in range(b-a+1):
        reverse_list[-x-1]=n_list[a+x-1]
    for x in range(b-a+1):
        n_list[a-1+x]=reverse_list[x]
for x in n_list:
    print(x, end=' ')
#1546
N=int(input())
list_N=list(map(int,input().split()))
max_score=max(list_N)
sum_new_score=sum(list_N)*100/max_score
ave_sum=sum_new_score/N
print('%.2f'%ave_sum)