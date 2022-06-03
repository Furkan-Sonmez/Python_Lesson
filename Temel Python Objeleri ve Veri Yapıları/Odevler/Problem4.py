
"""
Kullanıcıdan ad,soyad ve numara bilgisini alarak bunları alt alta ekrana yazdırın.
"""

AD=input("Lütfen adınızı yazınız : ")
SOYAD= input ("lütfen soyadınızı yazınız :")
NUMARA= input ("lütfen telefon numaranızı yazın :")

Bilgiler = [AD,SOYAD,NUMARA]

print("{}\n{}\n{}".format(Bilgiler[0],Bilgiler[1],Bilgiler[2]))
