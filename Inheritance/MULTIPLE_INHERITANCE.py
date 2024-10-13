# MULTIPLE INHERITANCE
class Father:
    def method3(self):
        print("im a father")
class Mother:
    def method3(self):
        print("im a mother")
class Child(Father,Mother):
    def method4(self):
        print("im a child")
child1=Child()
child1.method4()
child1.method3()
print(Child.__mro__)

""" 
While inheriting if we have 2 or more methods with same name then we use the "MRO"--METHOD RESOLUTION ORDER
It checks for methods in child first then it goes in  order that mentioned in derived class which parent is 
inherited first it checks the method in that parent class if found prints it or goes with next parent class
example:(<class '__main__.Child'>, <class '__main__.Father'>, <class '__main__.Mother'>, <class 'object'>)
"""