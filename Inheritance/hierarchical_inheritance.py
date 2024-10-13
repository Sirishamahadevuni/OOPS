""" using one parent class and deriving more than one child class is called hierarchical inheritance where the 
derived classes can use the methods and attributes of the parent class
"""
class Parent:
    def method(self):
        print("im a parent")
class child1(Parent):
    def method2(self):
        print("im child1")
class child2(Parent):
    def method3(self):
        print("im child2")
Child1=child1()
Child2=child2()
Child1.method()
Child1.method2()
Child2.method()
Child2.method3()


        