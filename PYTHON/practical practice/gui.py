d1={}
l1=[]
i=0
while(i<=5):
    l1.append(input("enter value in key-value pairs:"))
    i=i+1
d1.update(l1)
t1=tuple(l1)
size_tuple=len(t2)
k=1
temp=0
def sortdic():
    for i in range(0,size_tuple):
        for j in range(0,size-i):
            if(l1[j][k]>l1[j+1][k]):
                temp=l1[j][k]
                l1[j][k]=l1[j+1][k]
                l1[j+1][k]=temp
    d1.update(t2)
            

def displayy():
    print("the sorted disctionary is:")
    for i in range(0,size_tuple):
        print(d1[i], end=" ")
    
   
    
    
    
