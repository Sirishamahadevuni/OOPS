""" poly means many 
morphism means forms
polymorphism--having many forms
operator overloading is type of polymorphism ex:addition where it adds integer and for strings it concatinates
one operator have different functions so it is called polymorphism
definition: an ability can do more than one task

There are 2 types of polymorphism 
1.compile time polymorphism or static polymoriphism(method overloading,operator overloading binds at compile tym)
2.runtime polymorphism or dynamic polymorphism(binds at runtym "print function" decides at runtym)
polymorphism in functions:
"print" can print string, objects, integers....
#print(1,2,3,'hi',30.0) can print any type of datatype
 
 """

# def sum(*args):
#     if args:
#         start=type(args[0])()
#         for i in args:
#             start+=i
#         return start
# print(sum(1,2,3))
# print(sum([2,3,4],[8,5,4]))
# print(sum('hi','hello'))
class A:
    def fun(self):
        print("this is a's method")
class B:
    def fun(self):
        print("this is b's method")
class c:
    def fun(self):
        print("this is c's method")
        
def poly(obj):
    obj.fun()
obj1=A()
obj2=B()
obj3=c()
poly(obj1)
poly(obj2)
poly(obj3)