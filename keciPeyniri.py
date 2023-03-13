from decorator import Decorator


class KeciPeyniri(Decorator):
            def __init__(self):
                super().__init__()
                self.price = 12
                self.aciklama = "Keci peyniri"
        
    
            def getDescription(self):
                super().getDescription()
                self.aciklama = "Keci peyniri"
                
                return self.aciklama
        
    
            def getCost(self):
                super().getCost()
                self.price = 12
                
                return self.price