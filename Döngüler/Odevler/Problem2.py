
"""
Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulmaya çalışın.

Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 4. kuvvetinin toplamı( 3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse bu sayıya "Armstrong" sayısı denir.

Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4
"""

while True:
    istenen=input("""
    Uygulamadan çıkmak için q ya basın 
    
    Denemek istediginiz sayıyı yazınız: """)
    if (istenen == "q"):
        print("\tUygulama duruduruldu")
        break
    else:
        istenen = int (istenen)
        if(istenen<=0):
            print ("\n\t0 Dan Büyük bir sayı girin lütfen ")
        else :
            istenen=str(istenen)
            sayı_uzunlugu=0
            sayı_uzunlugu=len(istenen)
            istenen=int(istenen)
            gecici_sayı = istenen
            toplam=0
            while (gecici_sayı > 0):
    
                basamak = gecici_sayı % 10
    
                toplam += basamak ** sayı_uzunlugu
    
                gecici_sayı //= 10   
        if (toplam == istenen):
            print("\n\t",istenen,"bir armstrong sayısıdır.")
        else:
            print("\n\t",istenen,"bir armstrong sayısı değildir.")
              

           
