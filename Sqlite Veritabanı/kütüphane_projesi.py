# -*- coding: utf-8 -*-
from kütüphane import * 

print ("""*****************************************
       Kürüphane Programına Hoşgeldiniz. 
       
       İşlemler :
           1. Kitap Göster 
           2. Kitap Sorgula 
           3. Kitap Ekle 
           4. Kitap Sil 
           5. Baskı güncelle 
           Çıkmak için q ya basın 
           
*********************************************"""  )


while True : 
    işlem = input ("Yapacağınız işlem:")
    if (işlem == "q"):
        print ("Program Sonlandırılıyor.....")
        break
    elif (işlem == "1"):
        kütüphane.kitapları_goster()
    elif (işlem == "2"):
        isim = input ("Hangi kitabı istiyorsunuz ? ")
        print ("Kitap sorgulanıyor ")
        time.sleep(2)
        
        Kütüphane.kitap_sorgula(isim) 
    elif (işlem == "3"):
        isim = input ("isim:")
        yazar = input ("yazar:")
        yayınevi = input ("yayınevi:")
        tür = input ("tür:")
        baskı = int(input("baskı"))
        
        yeni_kitap = Kitap(isim,yazar,yayınevi,tür,baskı)
        
        print ("kitap ekleniyor... ")
        time.sleep(2)
        Kütüphane.kitap_ekle( yeni_kitapkitap)
        print ("kitap eklendi")
        
    elif (işlem == "4"):
        isim = input ("hangi kitabı silmek istiyorsunuz :")
        cevap = input ("Emin misiniz ? (E/H)")
        if (cevap == "E"):
            print ("kitap siliniyor ")
            Kütüphane.kitap_sil( isim)
            
            print ("Kitap silindi")
        else :
            print ("işlem iptal edildi.")
            break
            
    elif (işlem == "5"):
        pass
    else :
        print ("Geçersiz işle....")