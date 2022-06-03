
"""
Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.

*Beden Kitle İndeksi : Kilo / Boy(m) * Boy(m)
"""

print("*** Beden kitle indeksi bulan uygulamaya hoş geldiniz ***")

Kilo=  float (input("Lütfen Kilonuzu kg cinsinden giriniz : "))
Boy= float (input ("Lütfen boyunuzu cm cinsinden giriniz : "))

print ("Beden kitle indexsiniz : {}".format(Kilo/(Boy/100*Boy/100)) )