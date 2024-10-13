#put single underscore before data and method to declare as protected
class Parent:
    _protectedData=10
    def publicMethod(self):
        print(self._protectedData)
class Child(Parent):
    def method(self):
        print(self._protectedData)
obj1=Parent()
obj1.publicMethod()
print(obj1._protectedData)
obj2=Child()
obj2.method()
print(obj2._protectedData)