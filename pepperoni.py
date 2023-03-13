from pizza import Pizza


class Pepperoni(Pizza):

        def __init__(self):
            super().__init__()
            self.price = 68
            self.aciklama = " dana eti  ve baharat karisimiyla yapilan baharatli bir pizza..."
    
    
        def getDescription(self):
            super().getDescription()
            self.aciklama= " dana eti  ve baharat karisimiyla yapilan baharatli bir pizza..."
            return self.aciklama
        
    
        def getCost(self):
            super().getCost()
            self.price = 68
            return self.price
        
