#__ is used before the variables "to specify the user to use the variables more carefully since in python variables can access 
# to handle the important data we use this acess specifiers to specify users to handle carefully
class Parent:
    __privateData=10
    def publicMethod(self):
        print(self.__privateData)
class Child(Parent):
    def method(self):
        print(self.__privateData)
obj1=Parent()
obj1.publicMethod()
print(obj1.__privateData)
obj2=Child()
obj2.method()
print(obj2.__privateData)