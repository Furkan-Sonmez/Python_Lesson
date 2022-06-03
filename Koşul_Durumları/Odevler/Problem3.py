
"""
Kullanıcının girdiği vize1,vize2,final notlarına notlarına göre harf notunu hesaplayın.

    Vize1 toplam notun %30'una etki edecek.

    Vize2 toplam notun %30'una etki edecek.

    Final toplam notun %40'ına etki edecek.

    Toplam Not >=  90 -----> AA

    Toplam Not >=  85 -----> BA

    Toplam Not >=  80 -----> BB

    Toplam Not >=  75 -----> CB

    Toplam Not >=  70 -----> CC

    Toplam Not >=  65 -----> DC

    Toplam Not >=  60 -----> DD

    Toplam Not >=  55 -----> FD

    Toplam Not <  55 -----> FF
"""
print("**Harf Notunu Bulan uygulama**")

vize1=float(input("Lütfen 1. Vize Notunuzu Giriniz : "))
vize2= float(input("Lütfen 2. Vize Notunuzu Giriniz : "))
final= float(input("Lütfen Final Notunuzu Giriniz : "))

ort= vize1 * 30/100 + vize2*30/100 + final*40/100

if (ort >= 90 ):
    print("Harf Notunuz : AA Ortalamanız : {}".format(ort))
elif(ort>=85 and ort<90):
    print("Harf Notunuz : BA Ortalamanız : {}".format(ort))
elif(ort>=80 and ort<85):
    print("Harf Notunuz : BB Ortalamanız : {}".format(ort))
elif(ort>=75 and ort<80):
    print("Harf Notunuz : CB Ortalamanız : {}".format(ort))
elif(ort>=70 and ort<75):
    print("Harf Notunuz : CC Ortalamanız : {}".format(ort))
elif(ort>=65 and ort<70):
    print("Harf Notunuz : DC Ortalamanız : {}".format(ort))
elif(ort>=60 and ort<65):
    print("Harf Notunuz : DD Ortalamanız : {}".format(ort))
elif(ort>=55 and ort<60):
    print("Harf Notunuz : FD Ortalamanız : {}".format(ort))
else : 
    
    print("Harf Notunuz : FF Ortalamanız : {}".format(ort))