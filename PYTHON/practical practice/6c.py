f=open("D:\\backup\\Aditya\\file2.txt","r+")
a=int(input("enter how many lines to read from the end:"))
l1=f.readlines()
print(l1)
size=len(l1)
f.close()
f=open("D:\\backup\\Aditya\\file2.txt","r+")
i=1
while (i<=size-a):
    f.readline()
    i=i+1
print(f.read())
f.close()

      
