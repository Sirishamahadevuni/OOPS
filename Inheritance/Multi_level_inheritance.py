"""   PARENT CLASS
           |
      CHILD CLASS(can extract only parent class)
           |
      Child class(can extract child and parent class)
"""
class Grandparent:
    def method1(self):
        print("im grand parent")
class parent(Grandparent):
    def method2(self):
        print("Im parent")
class child(parent):
    def method3(self):
        print("Im child")
child1=child()
child2=parent()
child1.method1()
child1.method2()
child1.method3()
child2.method1()
print(child.__mro__)
print(parent.__mro__)