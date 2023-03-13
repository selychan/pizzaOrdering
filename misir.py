from decorator import Decorator


class Misir(Decorator):
            def __init__(self):
                super().__init__()
                self.price = 5
                self.aciklama = "Misir"
        
    
            def getDescription(self):
                super().getDescription()
                self.aciklama = "Misir"
                
                return self.aciklama
        
    
            def getCost(self):
                super().getCost()
                self.price = 5
                
                return self.price