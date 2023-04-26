#백준 알고리즘 단계별로 풀기
#파이썬
#심화 1
#25083
print("         ,r'\"7")
print("r`-_   ,'  ,/")
print(" \\. \". L_r'")
print('   `~\\/')
print('      |')
print('      |')
#3003
m=list(input().split())
m_int=[]
for x in m:
    m_int.append(int(x))
chess_num=[1,1,2,2,2,8]
for x in range(6):
    if m_int[x]==chess_num[x]:
        print(0,end=' ')
    else:
        print(chess_num[x]-m_int[x],end=' ')
#2444
a=int(input())
for x in range(a):
    print(' '*(a-x-1),end="")
    print('*'*(2*x+1))
for x in range(a-1):
    print(' '*(x+1),end="")
    print('*'*(2*a-2*x-3))
#10812
b,c=map(int,input().split())
d=list(range(1,b+1))
for _ in range(c):
    e,f,g=map(int,input().split()) #e: 시작 바구니, f: 끝 바구니, g: 기준 바구니
    d=d[:e-1]+d[g-1:f]+d[e-1:g-1]+d[f:]
for x in d:
    print(x,end=' ')
#10988
def pellindrom(s):
    for x in range(len(list(s))//2):
        if s[x]!=s[-x-1]:
            return 0
    return 1

h=input()
print(pellindrom(h))
#1157
x=input()
x_upper=x.upper()
x_upper_list=list(x_upper)
abc_list=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
count_list=[]
for a in abc_list:
    cnt=0
    for m in range(len(x_upper_list)):
        if a in x_upper_list[m]:
            cnt=cnt+1
    count_list.append(cnt)
if count_list.count(max(count_list))!=1:
    print('?')
else:
    print(abc_list[count_list.index(max(count_list))])
#4344
C=int(input())
for x in range (C):
    N=list(map(int,input().split()))
    N_score=list(N[1:])
    N_ave=sum(N_score)/len(N_score)
    cnt=0
    for a in range(len(N_score)):
        if N_score[a]>N_ave:
            cnt=cnt+1
    ave_percent=cnt/len(N_score)*100
    print('%.3f%%'%ave_percent)
#2941
x=input()
y=['c=','c-','dz=','d-','lj','nj','s=','z=']
for a in y:
    if a in x:
        x=x.replace(a,'1')
print(len(x))
#1316
n=int(input())
m=1
alphabet='abcdefghijklmnopqrstuvwxyz'
alphabet_list=list(alphabet)
cnt=0
while m<=n:
    count=0
    x=input()
    x_list=list(x)
    x_result_list=[]
    for a in range (len(x_list)-1):
        if x_list[a]!=x_list[a+1]:
            x_result_list.append(x_list[a])
    x_result_list.append(x_list[len(x_list)-1])
    for b in alphabet_list:
        if x_result_list.count(b)>=2:
           count=count+1
    if count==0:
        cnt=cnt+1
    m=m+1
print(cnt)
#25206
score_dict={"A+":4.5,"A0":4.0,"B+":3.5,"B0":3.0,"C+":2.5,"C0":2.0,"D+":1.5,"D0":1.0,"F":0.0}
cnt=0
sum=0
for _ in range(20):
    i,j,k=input().split()
    j=float(j)
    if k!="P" :
        cnt+=j
        sum+=score_dict[k]*j
print("%.6f"%(sum/cnt))



