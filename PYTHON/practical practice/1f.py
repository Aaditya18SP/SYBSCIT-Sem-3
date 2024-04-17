a=int(input("enter the number to find the factorial for:"))
def factorial_re(a):
    if a==1:
        return 1
    else:
        var=a*factorial_re(a-1)
        return var
f=factorial_re(a)
print("the factorial is:",f)
        
    
    
    
    
          
