""" Inheritance is introduced to remove code duplicates and also to maintain the relationship between objects
example: University project 
Faculty Attributes:                     Behaviours:
1.First Name                          getFullName() 
2.Last Name                           changeAddress()
3.Email                               chanceNumber()
4.Faculty Id                          getsalary()
5.Mobile Number         
6.Address
7.Subjects Teaching
8.Salary
9.date joined

Faculty Attributes:                     Behaviours:
1.First Name                          getFullName() 
2.Last Name                           changeAddress()
3.Email                               chanceNumber()
4.student Id                          getGPA()
5.Mobile Number         
6.Address
7.Subjects Learning
8.GPA
"""
class Member:
    def __init__(self,firstname,lastname,email,memberid,mobileno,address):
        self.firstname=firstname
        self.lastname=lastname
        self.email=email
        self.memberid=memberid
        self.mobilen0=mobileno
        self.address=address
        
    def getFullname(self):
        print(self.firstname +''+self.lastname)
    def changeAddress(self,newaddress):
        self.address=newaddress
        print("Address Changed Successfully")
    def changeNumber(self,newnumber):
        self.mobilen0=newnumber
        print("Mobile number changed Successfully")
    def getdetails(self):
        print("Full name",self.firstname +''+self.lastname)
        print("address:",self.address)
        print("email",self.email)
        print("memberid",self.memberid)
        print("mobile_number:",self.mobilen0)
        
class Faculty(Member):
    def __init__(self,firstname,lastname,email,memberid,mobileno,address,subjectsteaching,salary):
        self.subjectsteaching=subjectsteaching
        self.salary=salary
        Member.__init__(self,firstname,lastname,email,memberid,mobileno,address)
    
    def getSalary(self):
        print("Your salary is:",self.salary)

class student(Member):
    def __init__(self,firstname,lastname,email,memberid,mobileno,address,subjects_learniing,GPA):
        self.subjects_learning=subjects_learniing
        self.GPA=GPA
        Member.__init__(self,firstname,lastname,email,memberid,mobileno,address)
    def getGPA(self):
        print("Your GPA is:",self.GPA)

Student_1=student('Mahadevuni','sirisha','sirishamahadevuni02@gmail.com','21311a1901','8787878787','abc','ecm',8.45)
Student_1.getFullname()
Student_1.getGPA()
Student_1.getdetails()  #similarly can do for faculty details
      