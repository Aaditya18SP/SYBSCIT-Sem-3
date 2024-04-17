d1={1:10,2:5,3:15,4:20,5:100,6:2,7:8,8:50}
s=len(d1)
i=1
total=0
while (i<s):
    total=total+d1[i]
    i=i+1

print(d1)
print("the sum of all items in the dictionary is:",total)
