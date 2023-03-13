from decorator import Decorator


class MozarellaPeyniri(Decorator):
            def __init__(self):
                super().__init__()
                self.price = 15
                self.aciklama = "Mozarella peyniri"
        
    
            def getDescription(self):
                super().getDescription()
                self.aciklama = "Mozarella peyniri"
                
                return self.aciklama
        
    
            def getCost(self):
                super().getCost()
                self.price = 15
                
                return self.price