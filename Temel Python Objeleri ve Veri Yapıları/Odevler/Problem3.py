
"""
Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın ve sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın.
"""

print ("Kilometrede yakılan yakıtı bulan uygulama ")

yakıt_fiyatı= float (input ("Lütfen yakıtınızın fiyatını yazınız(tl cinsinden) : "))
litre_yaktıgı= float (input ("Lütfen 100 km de kaç lütre yaptıgnızı girin : "))

print ("Aracınız 1 km mesafede :{}tl".format((litre_yaktıgı*yakıt_fiyatı)/100))
