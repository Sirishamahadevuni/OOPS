"""
Creation of Method in Class:
def methodname(self,keywords):
    #code here
to access the method we use objectname.method(keywords)
object_name.method()


"""

# class SampleClass:
#     def sampleMethod(self):
#         print("This method is created to demonstrate methods in class")

# new_object1=SampleClass()
# new_object1.sampleMethod() #it is printing what is present inside the method

"""
__init__() method:
we can use it to initialize the object when it is created .
when we use it inside the class it will automatically called when the class is called.
it is also reffered as constructor ,reusable attributs are used in this method.

syntax:
def __init__(self,parameter1......parametern):
    self.parameter1=parameter1
    self.parameter2=parameter2
                .
                .
                .
    self.parameterN=parameterN     
"""

class Constructor:
    def __init__(self):
        print("This method was called automatically when the class is created")
Constructor()