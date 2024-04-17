class course:
    def c_details(self,cname,cid):
        self.cname=cname
        self.cid=cid
class person:
    def getinfo(self,name,age):
        self.name=name
        self.age=age
class student(course,person):
    def getinfo2(self,name,age,rollno,cname,cid):
        self.rollno=rollno
        person.getinfo(self,name,age)
        course.c_details(self,cname,cid)
    
class fees(student):
    def getinfo(self,name,age,rollno,cname,cid,amount):
        student.getinfo2(self,name,age,rollno,cname,cid)
        self.amount=amount
    def displayinfo(self):
        print("The details are:")
        print("Name of student:",self.name)
        print("Age of student:",self.age)
        print("Rollno of student:",self.rollno)
        print("Course of student:",self.cname)
        print("Course id:",self.cid)
        print("Fees amount:",self.amount)
        
s1=fees()
s1.getinfo("Rajiv","20 years","A001","BSCIT",44,18000)
s1.displayinfo()
        
        
        
        
