from decorator import Decorator


class Sogan(Decorator):
            def __init__(self):
                super().__init__()
                self.price = 4
                self.aciklama = "Sogan"
        
    
            def getDescription(self):
                super().getDescription()
                self.aciklama = "Sogan"
                
                return self.aciklama
        
    
            def getCost(self):
                super().getCost()
                self.price = 4
                
                return self.price