d1={1:343,2:43,3:87,4:6,5:100}
s=['a','b','c']
l1=list(d1.values())
a=enumerate(s)
print("the sum of its elemets is:",list(a))

sum1=0
for i in range(1,len(d1)+1):
    sum1=sum1+d1[i]
print("the sum of its elemets is:",sum1)
