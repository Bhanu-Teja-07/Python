class father:
    def method1(self):
        print(" i am father")
class mother:
    def method2(self):
        print("i am mother")
class child(father,mother):
    def method3(self):
        print("i am child")
x=father()
y=mother()
z=child()
z.method3()
z.method1()
z.method2()
y.method2()
y.method3()


class grand_parent:
    def _init_(self,name):
        self.name=name
    def show(self):
        print(f"my name is {self.name}")
class parent(grand_parent):
    def _init_(self, name,age):
        self.name=name
        self.age=age
    def show1(self):
        print(f"my name is {self.name} and i am {self.age} year old")
class child(parent):
    def _init_(self, name, age,loc):
        self.name=name
        self.age=age
        self.loc=loc
    def show2(self):
        print(f"my name is {self.name} and i am {self.age} old, i live in {self.loc}")
z=grand_parent("rohit")
x=parent("ram",23)
y=child("rohan",23,"hyd")
y.show1()
y.show()
y.show2()
x.show1()

#Hierarchical Inheritance: 
# parent class
class Manager: 
   def managerMethod(self):
      print ("I am the Manager")

# child class
class Employee1(Manager): 
   def employee1Method(self):
      print ("I am Employee one")
      
# second child class
class Employee2(Manager): 
   def employee2Method(self):
      print ("I am Employee two")      

# creating instances 
man=Manager()
emp1 = Employee1()  
emp2 = Employee2()
# method calls
man.managerMethod()
man.employee1method()
emp1.managerMethod() 
emp1.employee1Method()
emp2.managerMethod() 

emp2.employee2Method()
emp1.employee2Method()


#Hybrid Inheritance 
# parent class
class CEO: 
   def ceoMethod(self):
      print ("I am the CEO")
      
class Manager(CEO): 
   def managerMethod(self):
      print ("I am the Manager")

class Employee1(Manager): 
   def employee1Method(self):
      print ("I am Employee one")
      
class Employee2(Manager, CEO): 
   def employee2Method(self):
      print ("I am Employee two")      

# creating instances 
emp = Employee2()
# method calls
emp.managerMethod() 
emp.ceoMethod()
emp.employee2Method()