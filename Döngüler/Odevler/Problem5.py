
"""1'den 100'e kadar olan sayılardan sadece 3'e bölünen sayıları ekrana bastırın. Bu işlemi continue ile yapmaya çalışın."""
def bölme(sayı,denenen):
    bölme = sayı / denenen
    print ("Bölme işleminin sonucu =",bölme)
def Bölünür():
    print ("Sayı Tam Bölünüyor")
def Bölünmez():
    print("Sayı Tam Bölünmüyor")
def deneme(denenen):
    if (sayı%denenen==0):
        Bölünür()
    else :
        Bölünmez()
    bölme(sayı,denenen)

print("Bölüne bilme uygulamasına hoşgeldiniz")
while True:
    sayı=int (input ("Denemek istediginiz sayıyı giriniz : "))
    denenen=int (input("Hangi sayıya denenmesini istiyorsunuz : "))
    sayı =abs(sayı)
    denenen=abs (denenen)
    deneme(denenen)
    a=input ("uygulamayı sonlandırmak için q ya basın devam etmek içi herhangi bir tuşa basın lütfen : ")
    if(a=="q"):
        break
    else:
        continue
    

    
       


