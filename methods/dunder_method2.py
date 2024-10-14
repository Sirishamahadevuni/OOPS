class A:
    def __init__(self,a):
        self.a=a
    def __add__(self,object2):
        print(self.a+object2.a)
obj1=A(10)
obj2=A(20)
obj1+obj2