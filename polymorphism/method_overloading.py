""" if the class contains more than one method has same name and the methodscontain different datatypes
of parameters (or) different number of parameters (or) Both is called Method Overloading

same method with different datatypes of parameters:
class A:
    def method(int,int):
        pass
    def method(str,str):
        pass
    def method(float,float):
        pass
        
same method with different number of parameters:
class A:
    def method(int):
        pass
    def method(int,int):
        pass
    def method(int,int,int):
        pass
        
same method with different data types and diff number of parameters:
class A:
    def method(int):
        pass
    def method(float,float):
        pass
    def method(str,str,str):
        pass
we use this to complete a task with different parameter size and diff dataypes by using one method
example:we want to perform addition for:
    3 integers,4 integers,10 float values,3 strings....
class D:
    def add(int,int):
        pass
    def add(int,int,int):
        pass
        ....
features of method overloading 1.Flexibility 2.Readability 3,program is easy to see complexity will decrease
 But python doesnt support method overloading because,python is dynamically typed language(doesnt check for data type and uses mro)
    
" To use methodoverloading we use multiple dispatch "
# class A:
#     def add(self,a,b):
#         return a+b
#     def add(self,a,b,c):
#         return a+b+c
# obj1=A()
# print(obj1.add(1,2,3))
# print(obj1.add(2,3))  """
import multipledispatch
class A:
    @multipledispatch.dispatch(int,int)
    def add(self,a,b):
        return a+b
    @multipledispatch.dispatch(int,int,int)
    def add(self,a,b,c):
        return a+b+c
    @multipledispatch.dispatch(str,str)
    def add(self,a,b):
        return a+b
obj1=A()
print(obj1.add(1,2,3))
print(obj1.add(2,3))
print(obj1.add('sirisha',' Mahadevuni'))