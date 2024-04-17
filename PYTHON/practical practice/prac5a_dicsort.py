d1={1:343,2:43,3:87,4:6,5:100}
l1=list(d1.items())
print(l1)
i=0
j=0
temp=0
size=len(l1)
while (i<size):
    for j in range(0,size-i-1):
        if(l1[j][1]>l1[j+1][1]):
            temp=l1[j]
            l1[j]=l1[j+1]
            l1[j+1]=temp
    i=i+1

print("The sorted dictionary is:\n")                
print(dict(l1))   
