class mobile:
    def __init__(self,price,model):
        self.price=price
        self.model=model
    def discountPrice(self):
        return self.price-self.price*(1/10)
    def commonmethod(self):
        return "this is common method1"
    def commonmethod2(self):
        return "this is common method2"
    def getprice(self):
        return self.price
    def getMode(self):
        return self.model
class IPhone(mobile):
    def __init__(self, price, model):
        super().__init__(price, model)
        def somemethod(self):
            return "some method"
        def somemethod2(self):
            return "some other method"
        def discountPrice(self):
            return self.price-self.price*(1/10)
    
class samsung(mobile):
    def __init__(self, price, model):
        super().__init__(price,model)
        def somemethod3(self):
            return "some method"
        def somemethod4(self):
            return "some other method"
iphone_obj1=IPhone(500000,1001)   
print(iphone_obj1.discountPrice())    
samsung_obj1=samsung(67000,101)
print(samsung_obj1.discountPrice()) 
            