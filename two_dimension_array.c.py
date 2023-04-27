#백준 알고리즘 단계별로 풀기
#파이썬
#2차원 배열
#2738
n,m=map(int,input().split())
result=[]
result_2=[]
for x in range(n):
    m_list=list(map(int,input().split()))
    result.append(m_list)
for x in range(n):
    m_list=list(map(int,input().split()))
    result_2.append(m_list)
result_3=[]
for x in range(n):
    for y in range(m):
        print(result[x][y]+result_2[x][y],end=' ')
    print()
#2566
list_x=[]
list_max=[]
for x in range(9):
    list_x.append(list(map(int,input().split())))
for x in range(9):
    list_max.append(max(list_x[x]))
print(max(list_max))
n=list_max.index(max(list_max))
m=list_x[n].index(max(list_max))
print(n+1,m+1)
#10798
word_list=[]
word_len=[]
for _ in range(5):
    a=list(input())
    word_list.append(a)
    word_len.append(len(a))
for x in range(min(word_len)):
    for y in range(5):
         print(word_list[y][x],end='')
for x in range(min(word_len),max(word_len)):
    for y in range(5):
        if len(word_list[y])>x:
            print(word_list[y][x],end='')
#2563
num=int(input())
num_list=[[0]*100 for _ in range(100)]
for x in range(num):
    m,n=map(int,input().split())
    for a in range(m,m+10):
        for b in range(n,n+10):
            num_list[a][b]=1
cnt=0
for x in range(100):
    cnt+=sum(num_list[x])
print(cnt)