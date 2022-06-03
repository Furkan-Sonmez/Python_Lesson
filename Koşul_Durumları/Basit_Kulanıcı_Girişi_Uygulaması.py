print("***Kullanııcı Girişi Uygulaması***")

Ad=input("Kulanıcı Adınızı Girin : ")
sifre=input("Şifrenizi Giriniz : ")

if(Ad=="furkan" and sifre =="1234"  ):
    print ("Giriş Başarılı")
elif(Ad=="furkan" and sifre!="1234" ):
    print("Şifreniz yanlış tekrar deneyiniz")
elif(Ad!="furkan" and sifre=="1234" ):
    print("Kulanıcı adınız yanlış tekrar deneyiniz")
else:
    print("Kulanıcı adı ve şidre yanlış")