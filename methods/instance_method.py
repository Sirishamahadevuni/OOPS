""" Types of methods
1.instance method
2.class method
3.static method

1.instance method:by default the methods we create in class are instance methods
we can call it simply as Method of object

instance methods are used to create/access/modify/delete attributes of objects
performs operations on objects

creating instance method syntax:
def methodname(self,parameter1,parameter2,parameter3.....parameterN):
    body of method
    
self--first parameter mandatory.object reference is implicitly stored in self helps to perform operations on objects
"""
from types import MethodType
class Employee:
    A=10
    #creating instance variable using instance method
    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary
    def instancemethod(self):
        print("instance method")
        print(self.id)
    def instancemethod2(self,a,b):
        print(a,b)
    def updateclassvariable(self,newvalue):
        self.__class__.A=newvalue
        print(self.A)
#calling instance method:obj.instancemethod(parameters)
obj=Employee('pavan','gf2357',100000)
print(obj.salary)
print(obj.id)
obj.instancemethod()
obj.instancemethod2(10,20)
obj.updateclassvariable(30)

def addingmethod(self):
    print("new method")
obj.newinstancemethod=MethodType(addingmethod,obj)
obj.newinstancemethod()