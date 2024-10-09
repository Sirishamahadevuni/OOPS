""" 
class: Blue print for Creating object,we create an object that have related properties and methods,
class will give the code reusabilty and maintainability feature.
creation of class:
class ClassName:
    statement1
    statement2
       .
       .
       .
    statement n
object:instance of the class,we can create any number of objects

"""
# Class Creation
class SampleClass:
    attribute1=10
    attribute2=20

obj1=SampleClass() #creation of object when class is called object will be created
obj2=SampleClass()
obj3=SampleClass()
#(printing the attributes of class using class)
#print(SampleClass.attribute1)
#print(SampleClass.attribute2)
#(printig the attributes of class using objects)
#print(obj1.attribute1)
#print(obj2.attribute2)

"""
changing the values of attributes using the objects
changing one object will not affect the other objects even though other objects created by same class
if we change through the class attribute after object attribute updation it will reflect on all objects

"""
obj1.attribute1=100
SampleClass.attribute1=1
print(obj1.attribute1)
print(obj2.attribute1)
print(obj3.attribute1)

