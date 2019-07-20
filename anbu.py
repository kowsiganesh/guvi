a,b=map(int,input().split())
x=[]
for i in range(a+1,b+1):
    if(i%2!=0):
     x.append(i)
print(*x,sep=" ")
