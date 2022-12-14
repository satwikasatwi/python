l=[]
n=int(input("no.of elements"))
for i in range (0,n,1):
    x=int(input("enter elements"))
    l.append(x)
print(l)
min1=l[0]
for i in range(1,n):
    if(l[i]<min1):
        min1=l[i]
print(min1)
max=l[0]
for i in range(1,n):
    if(l[i]>max):
        max=l[i]
print(max)
    
    
