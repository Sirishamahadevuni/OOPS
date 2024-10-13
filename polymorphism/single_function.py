class A:
    def add(self,*args):
        if args:
            start=type(args[0])()
            for i in args:
               start+=i 
            return start
obj1=A()
print(obj1.add(1,2))
print(obj1.add(2,3,4))
print(obj1.add('siri','maha'))
print(obj1.add([1,2,3],[4,5,6]))