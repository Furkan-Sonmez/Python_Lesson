class kitap:
    def __init__(self, isimi,yazar , sayfa_sayisi,tur):
        print ("init fonksiyonu")
        self.isim=isimi
        self.yazar=yazar 
        self.sayfa=sayfa_sayisi
        self.tur=tur 
    def __str__(self):
        return "İsim : {}\nYazar: {}\nSayfa sayısı: {}\nTürü: {}".format(self.isim,self.yazar,self.sayfa,self.tur)
    def __len__(self): 
        return self.sayfa 


istanbul_hatırası = kitap ("istanbul hatırası","Ahmet Ümit",561,"Polisiye")

print(istanbul_hatırası)
print (len(istanbul_hatırası))

