class Student:
    
    def __init__(self,name,rollNo,address,phoneno):
        self.name=name
        self.rollNo=rollNo
        self.address=address
        self.phoneno=phoneno
        self.schoolname='ABC'

s1=Student('a',3,'abc',9875675867)

s2=Student('b',4,'abc',9856657867)

s3=Student('c',5,'abc',9567588767)

for obj in (s1,s2,s3):
    print(obj.name)
    print(obj.rollNo)
    print(obj.address)
    print(obj.phoneno)
    print(obj.schoolname)