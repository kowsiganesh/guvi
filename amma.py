n=int(input())
temp=n
a=0
while(n>0):
    dig=n%10
    a=a*10+dig
    n=n//10
if(temp==a):
    print("yes")
else:
    print("no")
