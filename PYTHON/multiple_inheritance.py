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
    def displayinfo(self):
        print("The details are:")
        print("Name of student:",self.name)
        print("Age of student:",self.age)
        print("Rollno of student:",self.rollno)
        print("Course of student:",self.cname)
        print("Course id:",self.cid)
s1=student()
s1.getinfo2("Rajiv","20 years","A001","BSCIT",44)
s1.displayinfo()
