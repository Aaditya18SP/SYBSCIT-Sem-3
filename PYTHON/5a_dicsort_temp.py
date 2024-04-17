d1={}
l1=[]
i=0
while(i<5):
    
    #l1.append(input("enter value in key-value pairs:"))
    
    l1.append(tuple(input("enter value in key-value pairs:"))))
    i=i+1
def disp_list():
    print("the list is:")
    for i in range(0,5):
        print(l1[i], end=" ")
disp_list()
t1=tuple(l1)
def disp_tuple():
    print("\nthe tuple is:")
    for i in range(0,5):
        #print(t1[i][0], end=" ")
        print(t1[i], end=" ")
disp_tuple()


d1.update(t1)
print(d1)


temp=0
l2=list(d1.items())
size=len(l2)
def sortdic():
    for i in range(0,size):
        for j in range(0,size-i-1):
            if(l2[j][1]>l2[j+1][1]):
                temp=l2[j][1]
                
                l2[j][1]=l2[j+1][1]
                l2[j+1][1]=temp
    d1.update(l2)
            


print("the sorted disctionary is:")
print(d1, end=" ")
        
    
sortdic()


    
#(1,'a') (2,'b') (3,'c') (4,'d') (5,'e')   
    
