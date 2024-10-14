""" Factory methods: are used to create object using method
"are used to create class instance"
"""
import datetime
class Student:
    def __init__(self,name,id,age):
        self.name=name
        self.id=id
        self.age=age
        
    @classmethod
    def getageasdob(cls,name,id,age):
        return cls(name,id,datetime.datetime.now().year-age)
        
student1=Student.getageasdob('siri',1000,2000)
print(student1.name,student1.id,student1.age)
student2=Student('xyy','10002',40) 
print(student2.age,student2.id,student2.name)        