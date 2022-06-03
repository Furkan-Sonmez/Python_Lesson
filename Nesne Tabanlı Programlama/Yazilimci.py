
class Yazilimci (): 

    def __init__(self,isim="Bilgi yok" ,soyisim="Bilgi yok",numara="Bilgi yok",maaş="Bilgi yok",diller="Bilgi yok"):
        self.isim =isim
        self.soyisim=soyisim
        self.numara = numara 
        self.maaş = maaş 
        self.diller = diller 

    def bilgileri_goster(self):
        print ("""
        Yazılımcı objesinin özellikleri 

        isim : {}
        
        Soyisim : {}

        Numara : {}

        Maaş : {} 

        Bildiği diller : {}
        
        """.format(self.isim,self.soyisim,self.numara,self.maaş,self.diller ))
    
    def zam_yap (self , zam_miktarı ): 
        print ("Zam yapılıyor ...")
        self.maaş += zam_miktarı

    def dil_ekle(self,yeni_dil):
        print ("Dil ekleniyor...")
        self.diller.append(yeni_dil)



furkan = Yazilimci("Furkan","sönmez","05533179778",2000,["Python","C","C#"])
furkan.bilgileri_goster()
furkan.dil_ekle("GO lang")
furkan.bilgileri_goster()
furkan.zam_yap(500)
furkan.bilgileri_goster()

