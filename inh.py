'''class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        return f"My name is {self.name} I am {self.age} years old."

class Employee(Person):
    pass
p=Person("ram",25)
e=Employee("shiva",20)
print(p.show())


class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show_details(self):
        return f"My name is {self.name} I am {self.age} years old."
    
class employ(person):
    def __init__(self, name,job,age):
        self.name=name
        self.job=job
        self.age=age

p=person("ram",25)
e=employ("ravi","ITsector",23)
print(e.show_details())
'''

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show_details(self):
        return f"My name is {self.name} I am {self.age} years old and works in {self.job}"
    
class employ(person):
    def __init__(self, name,job,age):
        super().__init__(name,age)
        self.job=job

p=person("ram",25)
e=employ("ravi","IT sector",23)
#print(e.show_details())
print(p.show_details())
