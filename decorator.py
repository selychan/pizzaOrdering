from pizza import Pizza


class Decorator(Pizza):
    
            def __init__(self):
                super().__init__()
                self.price = 0
                self.aciklama = " "
    
    
            def getDescription(self):
                super().getDescription()
                self.aciklama = " "
                
                return self.aciklama
            
    
            def getCost(self):
                super().getCost()
                self.price = 0
                
                return self.price
    
    