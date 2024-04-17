class student:
    def __init__(self):
        name=input("Enter name:")
        rollno=input("Enter rollno:")
        self.rollno=rollno
        self.name=name
        
    def printdetails(self):
        print("student name:",self.name)
        print("student rollno:",self.rollno)
       
        
        
        
        
    
class marks:
    def __init__(self,sub1,sub2):
        self.sub1=sub1
        self.sub2=sub2
        total=self.sub1+self.sub2
        self.total=total
    def printmarks(self):
        print("Marks in maths:",self.sub1)
        print("Marks in science:",self.sub2)
        print("Total Marks:",self.total)
    
s1=student()
s1.printdetails()
s2=marks(39,38)
s2.printmarks()

        
        
        
