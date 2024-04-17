l1=[]
l2=[]
print("enter list 1:")
for i in range(0,5):
    l1.append(input())
print(l1)
print("enter list 1:")
for i in range(0,5):
    l2.append(input())
print(l2)
for j in l1:
    if(j in l2):
        print("common member")

