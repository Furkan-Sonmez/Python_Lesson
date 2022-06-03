import random 
import time 


class Kumanda() : 
    def __init__(self, tv_durum = "Kapalı",tv_ses=0, tv_kanal_listesi = ["Trt"] ,tv_kanal = "Trt" ):
        self.tv_durum = tv_durum 
        self.tv_ses = tv_ses 
        self.kanal_listesi = tv_kanal_listesi 
        self.kanal = tv_kanal 
    def tv_ac(self):

        if (self.tv_durum == "Açık"):
            print("Tv zaten açık")

        else : 
            print ("Tv kapatılıyor...")
            self.tv_durum = "kapalı"
    def ses_ayarları(self):
        while True: 
            cevap = input ("Sesi azalt : '<'\nSesi arttır: '>'\nçıkıs:q")

            if (cevap == ">"):
                if (self.tv_ses !=30 ):

                    self.tv_ses +=1 

                    print("Ses =",tv_ses)
                else : 
                   print ("Ses max seviyede ")

            elif (cevap == "<")  : 
               if (self.tv_ses !=0 ):

                    self.tv_ses -=1 

                    print("Ses =",tv_ses)
               else : 
                   print ("Ses min seviyede ")
            else :
                break
    def kanal_ekle(self,kanal_ismi):
        print("Kanal ekleniyor ... ")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
        print ("Kanal eklendi")
    def rasgele_kanal(self):
        rastgele = random.randint(0,len(self.kanal_listesi)-1)
        self.kanal = self.kanal_listesi[rastgele]

    def __len__(self):
        return len(self.kanal_listesi)
    def __str__(self):
        return "Tv Durumu : {}\nTv Ses: {}\nŞuanki kanal : {}\n".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)


kumanda1 = Kumanda() 
print("""
Televizyon uygulaması 

1. Tv Aç 
2. TV Kapat
3. Ses Ayarı
4. Kanal Ekle 
5. Kanal Sayısı Öğrenme 
6. Rastgele Kanal Geçme 
7. Tv bilgileri 

Çıkış için 'q' ya basın.... 
""")

while True :
    
    istek = input("Hangi işlemi yapmak istiyorsunuz:")
    if(istek == "q"):
        print ("program sonlandırılıyor...")
        break
    elif(istek == "1"):
       kumanda1.tv_ac()
    elif (istek == "2"):
       kumanda1.tv_kapat
    elif (istek  =="3" ):
        kumanda1.ses_ayarları()
    elif (istek == "4"):
        kanal_isimleri = input("Kanal isimlerini ',' ile ayırarak girin")
        kanal_listesi = kanalkanal_isimleri.split(",")
        for eklenecekler in kanal_listesi:
            kumanda1.kanal_ekle(eklenecekler)
    elif (istek == "5" ) :
        print ("kanal sayısı :",len(kumanda1))
    elif (istek== "6"):
        kumanda1.rasgele_kanal()
    elif(istek== "7"):
        print(kumanda1)
    else : print(kumanda1)

             
            



