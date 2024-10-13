""" 
combination of more than one inheritance is called as hgybrid inheritance i.e combination of single,multilevel,multiple inheritance
"""
class grandparent:
    def method1(self):
        print("Im grand father")
class parent1(grandparent):
    def method2(self):
        print("Im parent 1")
class parent2:
    def method3(self):
        print(" Im parent2")
class child(parent1,parent2):
    def method4(self):
        print("im a child")
child1=child()
child1.method4()
child1.method3()
child1.method2()
child1.method1()