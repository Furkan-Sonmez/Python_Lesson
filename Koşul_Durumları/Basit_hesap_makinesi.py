
print("***Hesap makinesine hoş geldiniz***")
a=float(input("Birinci Sayıyı Giriniz:"))
b=float(input("İkinci Sayıyı Giriniz:"))
print("Yapmak istediğiniz işlemi seçniz lütfen")
i = input("1.Toplam\n2.Çıkarma\n3.Çarpma\n4.Bölme\nİşlem Numarası : ")

if (i == "1"):
    print("işlem sunucunuz {} + {} = {}".format(a,b,a+b))
elif(i == "2"):
    print("işlem sunucunuz {} - {} = {}".format(a,b,a-b))
elif(i == "3"):
    print("işlem sunucunuz {} x {} = {}".format(a,b,a*b))
elif(i == "4"):
    print("işlem sunucunuz {} / {} = {}".format(a,b,a/b))
else:
    print ("hatalı işlem girdiniz lütfen başka bi işlem giriniz")
