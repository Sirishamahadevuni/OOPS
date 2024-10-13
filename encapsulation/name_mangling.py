""" Name Mangling: declare data or method with atleast 2 leading underscores and atmost 1 trailing underscore
then it will replace to __className Nmame by the interpreter
__data_ "preceding" leading _ trailing ,_className Name 
 Name Mangling is used to acess private data"""

class A:
    __a=10            #mangled and becomes _A__a
    ___b=20           #_A___b
    ____c=30          #_A____c
    _____d=40         #_A_____d
    __e_=50
    __f__=60
    __g___=80
    ___h_=90
    _i_=100
    ___j___=200
    # which variable is mangled? to know this we have to pass this class in dir method--returns attributes and methods
    def getprivate(self):
        print(self.__a)

class B(A):
    def getprivatedata(self):  
        print(self._A__a)

obj1=A()
print(obj1._A__a)
obj2=B()
obj2.getprivatedata()
print(obj2._A__a)

