
print("""Mükkemmel sayı bulan ugulamaya hosgediniz 

Mükemmel sayı, sayılar teorisinde, kendisi hariç pozitif tam bölenlerinin toplamı kendisine eşit olan sayı. 
Diğer bir ifadeyle, bir mükemmel sayı, bütün pozitif tam bölenlerinin toplamının yarısına eşittir.

""")

while True:
    sayı = input("""\tUygulamadan çıkmak için q ya basın lütfen
    Araştırmak istediginiz sayıyı giriniz : """)
    if(sayı=="q"):
        print("Uygulama durduruldu...")
        break
    else: 
        Tam_bolen=[]
        toplam=0
        sayı = int(sayı)
        for i in range(1,sayı):
            if(sayı%i==0):
                Tam_bolen.append(i)
                print("Bölen = ",i)
            else:
                print("Bölemeyen = ",i)
        for i in Tam_bolen :
            toplam +=i
        if(toplam==sayı ):
                print("Sayı mükkemmel sayı")
                print (toplam)
        else:
                print("Sayı mükkemmel degil")
                print (toplam)

