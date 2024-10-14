""" When ever a variable is created for object then it is instance variable 
we can access instance variable in 2 ways:
self.variablename=variablename
"""
class A:
    def __init__(self,a,b):
        self.instancevariable1=a #self is the reference for object we can use self to create instance variable in another method tpp
        self.instancevariable2=b
obj=A(10,20)
print(obj.instancevariable1)
print(obj.instancevariable2)
#to create a instance variable we can use obj.variable=value
obj.instancevariable3=40 
#we cannot access one object attributes with another object
obj2=A(100,200)
print(obj2.instancevariable1,"this is object2")
#to update a instance variable:obj.variable=value
obj.instancevariable1=300
print(obj.instancevariable1)   