""" There are 3 types of variables they are 1.static variable or class variable 2.instance variable 3.local variable
LOCAL VARIABLE:variable which is declared inside the method is called local variables same as 
variable declaration on function

STATIC OR CLASS VARIABLE:variable which is declared outside the method and inside the class then it is called
class variable or static variable.
classname.variable=value --it is also class variable

Instance variable is nothing but attributes of objects
class variables is nothing but attributes of class
"""
class A:
    staticVariable1=10
    staticVariable2=20
    def samplemethod(self):
        print("sample method")
    def method1(self):
        print(self.staticVariable1)
        print(A.staticVariable1)
A.staticVariable1=30
# we can access static variable/class variable in 2 ways 
# 1.className.staticvariableName
print(A.staticVariable1)
print(A.staticVariable2)
#print(A.staticvariable3)
#another way:objectname.staticvariablename
obj=A()
print(obj.staticVariable1)
