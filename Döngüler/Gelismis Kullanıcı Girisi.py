
print("""
Kullanıcı Girişi Uygulamasına Hoşgeldiniz
""")

Kullanıcı_adı = "furkan"
Kullanıcı_sifresi="1234"

Giris_hakkı = 5

while True :
    Kullanıcı_ad = input("Lütfen kullanıcı adızını giriniz : ")
    Kulanıcı_sifre = input("Lütfen şifrenizi giriniz : ")
    if(Kullanıcı_ad == Kullanıcı_adı and Kullanıcı_sifresi == Kulanıcı_sifre):
        print("Girişiniz Başarılı")
        break
    elif(Kullanıcı_ad != Kullanıcı_adı and Kullanıcı_sifresi == Kulanıcı_sifre):
        print("Kullanıcı adınız yanlış")
    elif(Kullanıcı_ad == Kullanıcı_adı and Kullanıcı_sifresi != Kulanıcı_sifre):
        print("Şifreniz yalnış")
    else:
        print("Kullanıcı Adı ve Şifreniz yanlış")
    Giris_hakkı -= 1
    if(Giris_hakkı==0):
        print("Giriş hakkınız bitti")
        break
    
