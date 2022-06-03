"""
Şimdi de geometrik şekil hesaplama işlemi yapalım. İlk olarak kullanıcıdan üçgenin mi dörtgenin mi tipini bulmak istediğini sorun.

Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi , dikdörtgen mi yoksa sıradan bir dörtgen mi olduğunu bulmaya çalışın.

Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı , eşkenar mı yoksa sıradan bir üçgen mi olduğunu bulmaya çalışın. Eğer verilen kenarlar bir üçgen belirtmiyorsa, ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın.o

Üçgen belirtme şartını bilmiyorsunuz internetten bakabilirsiniz.

Ayrıca , bu problemde mutlak değer bulmaya ihtiyacınız olacak. Bunun için, Pythonda hazır bir fonksiyon olan abs() fonksiyonunu kullanabilirsiniz. Kullanımı şu şekildedir ;
"""

print("Geometrik şekil tanımlayan uygulama ")
print("1.Dörtgen\n2.Üçgen")
sekil=input("Hangi Şekli İstersiniz Şekil Numarasını İstersiniz : ")
while True : 
    if(sekil=="1"):

     kenar1=float(input("Kenar uzunlugu giriniz : "))
     kenar2=float(input("Kenar uzunlugu giriniz : "))
     kenar3=float(input("Kenar uzunlugu giriniz : "))
     kenar4=float(input("Kenar uzunlugu giriniz : "))
     if(kenar1 == kenar2 and kenar1 == kenar3 and kenar1==kenar4):
         print("Verdiğiniz degerlere göre bu şekil kare")
     elif(kenar1==kenar2 and kenar3==kenar4):
         print("Verdiğiniz degerlere göre bu şekil dikdörtgen")
     elif(kenar3==kenar2 and kenar1==kenar4):
         print("Verdiğiniz degerlere göre bu şekil dikdörtgen")
     elif(kenar1==kenar1 and kenar2==kenar4):
         print("Verdiğiniz degerlere göre bu şekil dikdörtgen")
     else :
         print ("Verdiginiz şekil dörtgen değil ")

    elif(sekil =="2"):
        kenar1 = float(input("lütfen bir kenarı giriniz : "))
        kenar2 = float(input("lütfen bir kenarı giriniz : "))
        kenar3 = float(input("lütfen bir kenarı giriniz : "))
        if(abs(kenar1+kenar2)>kenar3 and abs(kenar2+kenar3)>kenar1 and (kenar3+kenar1)>kenar2):
            if(kenar1==kenar2 and kenar2==kenar3 and kenar3==kenar1):
                print("Verdiğiniz degerlere göre üçgeniniz eşkenar üçgen")
            elif(kenar1==kenar2):
                print("Verdiğiniz degerlere göre üçgeniniz ikiz kenar üçgen")
            elif(kenar1==kenar3):
                print("Verdiğiniz degerlere göre üçgeniniz ikiz kenar üçgen")
            elif(kenar3==kenar2):
                print("Verdiğiniz degerlere göre üçgeniniz ikiz kenar üçgen")
        else:
            print("Verdiginiz degerler üçgen belirtmiyor")

     


     