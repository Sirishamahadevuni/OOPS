""" under methods:double underscores :if a method has double underscores in front and back it is dunder method
"__init__()--example of dunder method,these are default methods 
when you create a class these dunder methods will stay as default bcz in python every class we created 
is child class to object class,in object class we have dunder methods

even if you inherit or dont inherit the object class.The object class is parent class to the class we created

if parent class have methods then child class also have those methods

dunder methods are also called as magical methods or special methods
we use +,-,=,*,/,+=.....len,str,del....when we use then within class the dundermethods will call automatically
# """
# class A:
#     pass
# #print(dir(A))
# print(dir(object))
"""output:dir(A) ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', 
'__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', 
'__lt__','__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', 
'__static_attributes__', '__str__', '__subclasshook__', '__weakref__']


dir(object):['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
'__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__',
'__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
# """
# class A:
#     pass
# obj=A()
# print(str(obj)) #<__main__.A object at 0x0000019518156900> ,checks __str__() dundermethod

class A:
    def __str__(self):
        return "it is dunder method"
obj=A()
print(str(obj))  #__str__ method calls when we tried str(obj)

""" similary when we call class __init__() dunder method calls,len(obj)--__len__() method calls ,
in operator-- __contains__(),obj1+obj2--__add__()

this dunder method is used to override the built in operations we can use dunder methods

__abs__--abs(object)
__add__--a+b
__and__--a & b
__call__ --class A: /n pass/n obj=A() /n obj()"""