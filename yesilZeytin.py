from decorator import Decorator


class YesilZeytin(Decorator):
            def __init__(self):
                super().__init__()
                self.price = 7
                self.aciklama = "Yesil Zetin"
        
    
            def getDescription(self):
                super().getDescription()
                self.aciklama = "Yesil Zeytin"
                
                return self.aciklama
        
    
            def getCost(self):
                super().getCost()
                self.price = 7
                
                return self.price