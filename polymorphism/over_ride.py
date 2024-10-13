           
class Parent:
    def method(self):
        print("this is parent method")
class child(Parent):
    def method(self):
        #Parent.method(self)
        super().method()
        print("this is child method")
c=child()
c.method()
# #even method get overrides we class print them using this 2 methods
# # to access parentclass.method(self,arguments)
# #super().methodname(arguments)
