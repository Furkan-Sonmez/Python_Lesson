class çalışan () : 
    def __init__(self, isim , maaş ,departman ):
        print("Çalışan sınıfının init fonksiyonu... ")
        self.isim = isim 
        self.maaş = maaş 
        self.departman = departman 
    def bilgileri_goster(self): 
        print ("Çalışan sınıfının bilgileri ...")
        print ("isim : {}\nMaaş : {}\nDepartman : {}\n".format(self.isim,self.maaş,self.departman))
    def departman_degistir(self,yeni_departman): 
        self.departman = yeni_departman 

class yonetici (çalışan): #Miras aldık ordan yani yazmadan ordan kullandık
   
    def __init__(self, isim , maaş ,departman , kisi_sayisi ): #bunu aynı yaptığımda mirası iptal etmiş oluyorsun
        print("Yönetici sınıfının init fonksiyonu... ")
        self.isim = isim 
        self.maaş = maaş 
        self.departman = departman 
        self.kisi_sayisi= kisi_sayisi 
    
    def zam_yap(self,zam_miktarı):
        self.maaş += zam_miktarı



#Furkan_yönetici = yonetici ("furkan",3000,"Bilişim")
#Furkan_yönetici.bilgileri_goster()
#Furkan_yönetici.zam_yap(5500)
#Furkan_yönetici.bilgileri_goster()   


Ayse_yönetici = yonetici ("ayşe",4000,"bilişim",10)
Ayse_yönetici.bilgileri_goster()