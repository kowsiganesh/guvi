T,S=map(int,input().split())
arr=[]
arr=[int(i) for i in input().split()]
a=0
n=0
while S>0:
  n+=arr[a]
  S=S-1
  a=a+1
print(n)
