class person:
	def info(self,name,age):
		self.name=name
		self.age=age
class employee(person):
    def info(self,name,age,emp_id,salary):
        person.info(self,name,age)
        self.salary=salary
        self.empid=emp_id
    def displayinfo(self):
        print("The details are:")
        print("Name of employee:",self.name)
        print("Id of employee:",self.empid)
        print("Salary of employee:",self.salary)
        print("Age of employee:",self.age)
class student(person):
    def info(self,name,age,course,rollno):
        person.info(self,name,age)
        self.course=course
        self.rollno=rollno
    def displayinfo(self):
        print("The details are:")
        print("Name of student:",self.name)
        print("Rollno of student:",self.rollno)
        print("Course of student:",self.course)
        print("Age of student:",self.age)
        
        
    
e1=employee()
s1=student()
e1.info("Tony","30 years",202012,10000)
s1.info("Rajiv","20 years","BSCIT","A001")
e1.displayinfo()
s1.displayinfo()
