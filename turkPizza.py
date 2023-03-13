from pizza import Pizza


class TurkPizza(Pizza):

        def __init__(self):
            super().__init__()
            self.price = 70
            self.aciklama = " Pastirma,kasar peyniri zeytin ve mantar.."
    
    
        def getDescription(self):
            super().getDescription()
            self.aciklama= " Pastirma,kasar peyniri zeytin ve mantar.."
            
            return self.aciklama
        
    
        def getCost(self):
            super().getCost()
            self.price = 70
            
            return self.price
        




 