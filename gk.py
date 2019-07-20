x1,y1=map(int,input().split())
for a in range (x1+1,y1):
  for b in range (2,a):
    if (a%b==0):
      break
  else:
      print(a,end=" ")
