
"""
Kullanıcıdan 3 tane sayı alın ve en küçük sayıyı ekrana yazdırın.
"""

print("Sayı sıralama uygulaması")

a = float(input("Birinci sayıyı giriniz : "))
b = float(input("İkinci sayıyı giriniz : "))
c = float(input("Üçüncü sayıyı giriniz : "))

if (a<b and a<c):
    kucuk_sayı=a
elif (b<a and b<c):
    kucuk_sayı=b
elif (c<a and c<b):
    kucuk_sayı=c

print("En küçük sayı",kucuk_sayı)