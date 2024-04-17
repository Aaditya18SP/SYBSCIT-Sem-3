d1={1:10,2:5,3:15,4:20,5:100,6:2,7:8,8:50}
d2={}
s=len(d1)
i=1
j=1
#ascending
while (i<=s):
    j=1
    while(j<=s-1):
        if(d1[j]>d1[j+1]):
            t=d1[j]
            d1[j]=d1[j+1]
            d1[j+1]=t
        j=j+1
    i=i+1
print(d1)
d1={1:10,2:5,3:15,4:20,5:100,6:2,7:8,8:50}
#descending
i=1
j=1
while (i<=s):
    j=1
    while(j<=s-1):
        if(d1[j]<d1[j+1]):
            t=d1[j]
            d1[j]=d1[j+1]
            d1[j+1]=t
        j=j+1
    i=i+1
print(d1)
                   
    
    
