print("""
Furkan Banka Hoşgeldiniz
""")

Hesap_bakiye= 1000

Kullanıcı_adı = "furkan"
Kullanıcı_sifresi="1234"

Giris_hakkı = 5

while True :
    Kullanıcı_ad = input("Lütfen kullanıcı adızını giriniz : ")
    Kulanıcı_sifre = input("Lütfen şifrenizi giriniz : ")
    if(Kullanıcı_ad == Kullanıcı_adı and Kullanıcı_sifresi == Kulanıcı_sifre):
        print("Girişiniz Başarılı")
        print("1.Para Çekme \n2.Para Yatırma\n3.Başka Hesaba Para Transveri\nKartı Geri Almak İçin 'q' basınız")
        while True:
            secenek=input("Yapamak istediginiz işlemin numarasını giriniz : ")
            if(secenek=="q"):
                print("Kartınızı almayı unutmayın ")
                break
            elif(secenek=="1"):
                print("Hesap Bakiyeniz : ",Hesap_bakiye)
                Çekilecek_tutar=int(input("Çekmek istediğiniz tutarı giriniz : "))
                if(Çekilecek_tutar>Hesap_bakiye):
                    print("Hesabınızda Yeterince Bakiye Yok Tekarar İşlemlerinizi Gerçekleştiriniz")
                else: 
                    Hesap_bakiye -=Çekilecek_tutar
                    print("Çektiğiniz tutar = {} , Yeni hesap bakiyeniz = {}".format(Çekilecek_tutar,Hesap_bakiye))
            elif(secenek=="2"):
                print("Hesap Bakiyeniz : ",Hesap_bakiye)
                Yatırılacak_tutar=int(input("Hesaba yatırılacak tutarı giriniz : "))
                Hesap_bakiye+=Yatırılacak_tutar
                print("Yatırılacak tutar = {} , Yeni hesap bakiyeniz = {}".format(Yatırılacak_tutar,Hesap_bakiye))
            elif(secenek=="3"):
                print("Hesap Bakiyeniz : ",Hesap_bakiye)
                Yollanıcak_tutar=int(input("Yollıyacagınız tutarı giriniz"))
                iban=input("Yollamak istediginiz ibanı giriniz : ")
                if(Yollanıcak_tutar>Hesap_bakiye):
                    print("Hesabınızda Yeterince Bakiye Yok Tekarar İşlemlerinizi Gerçekleştiriniz")
                else: 
                    Hesap_bakiye -=Yollanıcak_tutar
                    print("Yollanan tutar = {} , Yeni hesap bakiyeniz = {}".format(Yollanıcak_tutar,Hesap_bakiye))
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
    