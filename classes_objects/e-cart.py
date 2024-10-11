class E_cart:
    def __init__(self):
        self.items=[]
    def add_item(self,product):
        self.product=product
        self.items.append(product)
        print("product added:",product)  
    def delete_item(self,product):
        self.product=product
        if self.product in self.items:
            self.items.remove(self.product)
        else:
            print("item didnt found")    
    def display(self):
        print("number of items in the cart",len(self.items))
        for item in self.items:
            print(item)
obj1=E_cart()
obj1.add_item('dress')
obj1.add_item('shoe')
obj1.add_item('toy')
obj1.delete_item('car')
obj1.display()
        
        