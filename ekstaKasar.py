from decorator import Decorator


class EkstraKasar(Decorator):
            def __init__(self):
                super().__init__()
                self.price = 10
                self.aciklama = "Eksta Kasar"
        
    
            def getDescription(self):
                super().getDescription()
                self.aciklama = "Ekstra Kasar"
                
                return self.aciklama
        
    
            def getCost(self):
                super().getCost()
                self.price = 10
                
                return self.price