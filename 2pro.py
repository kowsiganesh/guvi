N=int(input())
if(N==0):
    for i in range(0,5):
        print(0,end=" ")
else:        
    for j in range(1,(N*5)+1):
        if(j%N==0):
            print(j,end=" ")
