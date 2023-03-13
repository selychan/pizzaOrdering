from decorator import Decorator
from ekstaKasar import EkstraKasar
from keciPeyniri import KeciPeyniri
from klasik import Klasik
from margherita import Margherita
from metinolusturma import menu
from pepperoni import Pepperoni
from turkPizza import TurkPizza
from yesilZeytin import YesilZeytin
from keciPeyniri import KeciPeyniri
from mozarellaPeyniri import MozarellaPeyniri
from sogan import Sogan
from misir import Misir
import csv
import datetime

#sınıflardan objectler oluşturuldu.
pizza1 =Klasik()
pizza2 = Margherita()
pizza3 = TurkPizza()
pizza4 = Pepperoni()
misir1 = Misir()
sogan1 = Sogan()
mozarellaPeyniri1= MozarellaPeyniri()
keciPeyniri1 = KeciPeyniri()
ekstrakasar1 = EkstraKasar()
yesilZeytin1 = YesilZeytin()
decorator1 = Decorator()




#pizza fiyatini gösteren fonksiyon yazildi. pizza sos ve tabani seçildikten sonra toplam ödenecek tutar gösterildi.


def pizzaFiyatGöster():
     toplamFiyat = 0
     if secilenPizza == 1 :

          if secilenSos == 11 :
               toplamFiyat=ekstrakasar1.getCost() + pizza1.getCost()
               print(pizza1.getDescription()+ekstrakasar1.getDescription())
          elif secilenSos == 12 :
               toplamFiyat=yesilZeytin1.getCost() + pizza1.getCost()  
               print(pizza1.getDescription()+yesilZeytin1.getDescription())         
          elif secilenSos == 13 :
               toplamFiyat=keciPeyniri1.getCost() + pizza1.getCost() 
               print(pizza1.getDescription()+keciPeyniri1.getDescription())
          elif secilenSos == 14 :
               toplamFiyat=mozarellaPeyniri1.getCost() + pizza1.getCost() 
               print(pizza1.getDescription()+mozarellaPeyniri1.getDescription())
          elif secilenSos == 15 :
               toplamFiyat=sogan1.getCost() + pizza1.getCost() 
               print(pizza1.getDescription()+sogan1.getDescription())
          elif secilenSos == 16 :
               toplamFiyat=misir1.getCost() + pizza1.getCost() 
               print(pizza1.getDescription()+misir1.getDescription())

     elif secilenPizza == 2 :

          if secilenSos == 11 :
               toplamFiyat=ekstrakasar1.getCost() + pizza2.getCost()
               print(pizza2.getDescription()+ekstrakasar1.getDescription())
          elif secilenSos == 12 :
               toplamFiyat=yesilZeytin1.getCost() + pizza2.getCost() 
               print(pizza2.getDescription()+yesilZeytin1.getDescription())          
          elif secilenSos == 13 :
               toplamFiyat=keciPeyniri1.getCost() + pizza2.getCost() 
               print(pizza2.getDescription()+keciPeyniri1.getDescription())
          elif secilenSos == 14 :
               toplamFiyat=mozarellaPeyniri1.getCost() + pizza2.getCost() 
               print(pizza2.getDescription()+mozarellaPeyniri1.getDescription())
          elif secilenSos == 15 :
               toplamFiyat=sogan1.getCost() + pizza2.getCost() 
               print(pizza2.getDescription()+sogan1.getDescription())
          elif secilenSos == 16 :
               toplamFiyat=misir1.getCost() + pizza2.getCost()  
               print(pizza2.getDescription()+misir1.getDescription())      

     elif secilenPizza == 3 :

          if secilenSos == 11 :
               toplamFiyat=ekstrakasar1.getCost() + pizza3.getCost()
               print(pizza3.getDescription()+ekstrakasar1.getDescription())
          elif secilenSos == 12 :
               toplamFiyat=yesilZeytin1.getCost() + pizza3.getCost() 
               print(pizza3.getDescription()+yesilZeytin1.getDescription())          
          elif secilenSos == 13 :
               toplamFiyat=keciPeyniri1.getCost() + pizza3.getCost() 
               print(pizza3.getDescription()+keciPeyniri1.getDescription())
          elif secilenSos == 14 :
               toplamFiyat=mozarellaPeyniri1.getCost() + pizza3.getCost() 
               print(pizza3.getDescription()+mozarellaPeyniri1.getDescription())
          elif secilenSos == 15 :
               toplamFiyat=sogan1.getCost() + pizza3.getCost() 
               print(pizza3.getDescription()+sogan1.getDescription())
          elif secilenSos == 16 :
               toplamFiyat=misir1.getCost() + pizza3.getCost()   
               print(pizza3.getDescription()+misir1.getDescription())     

     elif secilenPizza == 4 :

          if secilenSos == 11 :
               toplamFiyat=ekstrakasar1.getCost() + pizza4.getCost()
               print(pizza4.getDescription()+ekstrakasar1.getDescription())
          elif secilenSos == 12 :
               toplamFiyat=yesilZeytin1.getCost() + pizza4.getCost() 
               print(pizza4.getDescription()+yesilZeytin1.getDescription())          
          elif secilenSos == 13 :
               toplamFiyat=keciPeyniri1.getCost() + pizza4.getCost()
               print(pizza4.getDescription()+keciPeyniri1.getDescription()) 
          elif secilenSos == 14 :
               toplamFiyat=mozarellaPeyniri1.getCost() + pizza4.getCost() 
               print(pizza4.getDescription()+mozarellaPeyniri1.getDescription())
          elif secilenSos == 15 :
               toplamFiyat=sogan1.getCost() + pizza4.getCost()
               print(pizza4.getDescription()+sogan1.getDescription()) 
          elif secilenSos == 16 :
               toplamFiyat=misir1.getCost() + pizza4.getCost() 
               print(pizza4.getDescription()+misir1.getDescription())    
                  
     print("Odeyeceginiz Toplam Tutar:")
     print(toplamFiyat)
     print("tl dir.")
     return toplamFiyat







secilenPizza = "secilen pizza"
secilenSos = "secilen pizza "
secilenPizza =int(input("Lütfen bir Pizza Tabani Seciniz: "))
secilenSos =int(input("Lütfen bir Sos Seciniz: "))
pizzaFiyatGöster()

mydict =[{'Kimlik No': input("Kimlik No:"), 'Kredi kart no': input("Kart no nuz:"), 'Kredi Kart Sifresi': input("kart sifreniz:"), 'Kullanici Adi': input("adiniz:"),'Siparis Aciklamasi':input("Siparis aciklamaniz:"),"Siparis Zamani":datetime.datetime.now()}] 
fields1 = ['Kimlik No','Kredi kart no','Kredi Kart Sifresi','Kullanici Adi','Siparis Aciklamasi','Siparis Zamani']

with open("Orders_Database.csv",'w') as csvfile:
     writer =csv.DictWriter(csvfile, fieldnames = fields1)
     writer.writeheader()
     writer.writerows(mydict)














































     



        







