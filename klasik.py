from pizza import Pizza


class Klasik(Pizza):
    


    
        def __init__(self):
            super().__init__()
            self.price = 45
            self.aciklama = " Sucuk,kasar peyniri ve domates salcasi...."
    
    
        def getDescription(self):
            super().getDescription()
            self.aciklama = " Sucuk,kasar peyniri ve domates salcasi...."
            return self.aciklama
        
    
        def getCost(self):
            super().getCost()
            self.price = 45
            return self.price
            
        
    



