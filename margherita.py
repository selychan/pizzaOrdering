from pizza import Pizza

class Margherita(Pizza):

            def __init__(self):
                super().__init__()
                self.price = 55
                self.aciklama = " domates, mozarella, fesleğen ile yapilan Napoli pizzasidir..."
        
    
            def getDescription(self):
                    super().getDescription()
                    self.aciklama= " domates, mozarella, fesleğen ile yapilan Napoli pizzasidir..."
                    print(self.aciklama)
                    return self.aciklama
                
    
            def getCost(self):
                super().getCost()
                self.price = 55
                return self.price

        
        
    