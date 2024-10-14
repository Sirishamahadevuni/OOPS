""" Any method we create with in class are called instance methods 
we can access class variables/methods using objects and access using class
class methods not only used for accessing class variables but also to deal with factory methods

why we create class methods??
to perform operations on class level variables and deal with factory methods

creating class method syntax : 
@classmethod <-- decorator
def methodName(cls,parameters):
    body
"""
class Student:
    college='xyz'
    @classmethod
    def classmethod1(cls):
        print("class method created successfully")
        #updating class variable
        cls.college='ABC'
        print(cls.college)
    
#accessing class method:object/classname.classmethod(arguments)
Student.classmethod1()
student1=Student()
student1.classmethod1()