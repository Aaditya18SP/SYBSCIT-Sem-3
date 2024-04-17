class person:
	def info(self,name,emp_id):
		self.name=name
		self.empid=emp_id
class employee(person):
    def info2(self,name,emp_id,salary):
        person.info(self,name,emp_id)
        self.salary=salary
    def displayinfo(self):
        print("The details are:")
        print("Name of employee:",self.name)
        print("Id of employee:",self.empid)
        print("Salary of employee:",self.salary)
e1=employee()
e1.info2("Arun",2020001,20000)
e1.displayinfo()
