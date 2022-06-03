try : 
    acılandosya =open("bilgiler.txt","w",encoding="utf-8") # encoding="utf-8" TÜRKÇE KARAKTER EKLEDİK , w kullanırsak her seferinde dosya silinir ve en baştan yazmamız gerekir sürekli , silinmesini istemiyorsak a yı kıllanmak lazım sonrasında sadece şlk açtığımızda kullanmak lazım aslında w yu 
    
    acılandosya.write("furkan sönmez\n")
    acılandosya.write("mehmet sallamasyon\n")
    
    acılandosya = open("bilgiler.txt","a",encoding = "utf-8") # eger a kipiyle açarsak append yani ekleme anlamına gelir. yani eski dosya silinmemiş olur. 
    acılandosya.write("Eklenen")

except : 
    print ("hata oldu")

finally :
   acılandosya.close() 