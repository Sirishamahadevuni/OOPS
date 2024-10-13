""" One of principle oops concept
combining related things into single unit
combining related data and methods written in class of a specific object is known as encapsulation
class is example of encapsulation
1.code will be organized and neet
2.prevents the data from accidental removal and deletion ex:pandas library we can use the lib but cant change or delete
3abstraction:we casn use it but we cant see the logic benind it
4.data hiding:access specifiers
5,Modularity:creating diff classes individuallyy ,reduces development cost
combination of data hing and abstracton is encapsulation

Access Modifiers:in java and c++
1.public --same class,access from subclass aceess by subclass (everywhere)
2.private --with in it class and the derived class from that
3.protected--within the class
in python private,protected data is accessed same as public data
"""
class Parent:
    publicData=10
    def publicMethod(self):
        print(self.publicData)
class Child(Parent):
    def method(self):
        print(self.publicData)
obj1=Parent()
obj1.publicMethod()
print(obj1.publicData)
obj2=Child()
obj2.method()
print(obj2.publicData)