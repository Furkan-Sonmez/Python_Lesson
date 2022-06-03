"""
Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın.

 Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)

 BKİ 18.5'un altındaysa -------> Zayıf

 BKİ 18.5 ile 25 arasındaysa ------> Normal

 BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

 BKİ 30'un üstündeyse -------------> Obez
 """
print("Beden kitle indexsini bulan uygulamaya hoşgeldiniz")

boy=float(input("Boyunuzu (m cinsinden giriniz) : "))
kilo=float(input("Kilonuzu (kg cinsinden giriniz) : "))

index= kilo/(boy**2)

if(index<18.5 ):
    print("Zayıfsınız Kilo Almanız Gerekiyor ")
elif(index>18.5 and index <= 25):
    print("Kilonuz gayet  normal ")
elif(index>25 and index < 30):
    print("Fazla Kilolusunuz ")
else : 
    print ("Obezsiniz kilo vermeniz lazım ")







