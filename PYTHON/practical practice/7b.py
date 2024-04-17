class person:
    def info(self,age):
        self.age=age;
class student(person):
    def info(self,age,name):
        person.info(self,age)
        self.name=name
    
class employee(person):
    def info(self,age,e_id):
        person.info(self,age)
        self.e_id=e_id
    
class player(student,employee):
    def info(self,age,name,e_id,pid):
        student.info(self,age,name)
        employee.info(self,age,e_id)
        
        self.pid=pid
    def printi(self):
        print("name is:",self.name)
        print("age is",self.age)
        print("eid is",self.e_id)
        print("player id is:",self.pid)
        
        
s1=player()
s1.info(18,'abc',10001,'p102')
s1.printi()
        
        
    
    
