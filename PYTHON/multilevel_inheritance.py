class person:
	def info(self,name,emp_id):
		self.name=name
		self.empid=emp_id
class employee(person):
    def info(self,name,emp_id,salary):
        person.info(self,name,emp_id)
        self.salary=salary
class post(employee):
    def info(self,name,emp_id,salary,position):
        employee.info(self,name,emp_id,salary)
        self.position=position
        
    def displayinfo(self):
        print("The details are:")
        print("Name of employee:",self.name)
        print("Id of employee:",self.empid)
        print("Salary of employee:",self.salary)
        print("Position of employee:",self.position)
e1=post()
e1.info("Tony",202012,10000,"accountant")
e1.displayinfo()
