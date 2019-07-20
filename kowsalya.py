k=str(input())
count=0
for i in k:
    if i.isnumeric() or i.isalpha():
        pass
    else:
        count+=1
print(count)
