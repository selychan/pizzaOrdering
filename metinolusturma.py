 

menu = open("C:/Users/sella/OneDrive/Masaüstü/PROJE/menu.txt","w")#kendi dizinime kaydettim o kısmı silip default da kaydetmesini sağlayabilriz.
menu.write("*Lutfen Bir Pizza Tabani Seciniz:\n" +
            "1: Klasik\n"+
            "2: Margarita\n"+
           "3: TurkPizza\n"+
           "4: Pepperoni Pizza\n"+
           "* ve sececeginiz sos:\n"+
           "11: Eksta Kasar\n"+
           "12:Yesil Zeytin\n"+
           "13: Keci Peyniri\n"+
           "14: Mozarella Peyniri\n"+
           "15: Sogan\n"+
           "16: Misir\n"+
        "Tesekkur ederiz!")
menu =open("menu.txt")
print(menu.read())
                




