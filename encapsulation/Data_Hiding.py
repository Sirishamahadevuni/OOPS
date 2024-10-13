""" This concept comes from encapsulation 
Data Hiding--- Declare data in one class ,doesnt give access to another clas & hides the data due to sensitive info
gives security to sensitive data
put __ double underscore in front of data
private data is only called with methods but not with ojects if we do so we get error
we can use namemangling for accessing the private data
"""

class Bank:
    __balance=1000
    def getbalance(self):
        return self.__balance
class AP(Bank):
    def printbalance(self):
        return self.__balance
obj=AP()
obj2=Bank()
print(obj.getbalance())
print(obj.printbalance()) #error