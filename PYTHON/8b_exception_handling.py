try:
    a=int(input("enter marks in maths:"))
    b=int(input("enter marks in science:"))
    c=a/b
    d=((a+b)/80)*100
    
except(ZeroDivisionError):
    print("cant divide by zero")
except(ValueError):
    print("Incorrect values entered")
except(TypeError):
    print("incorrect data type")
else:
    print("marks in maths:",a)
    print("marks in science:",b)
    print("Percentage is:",d)
finally:
    print("Total marks:",a+b)


    
