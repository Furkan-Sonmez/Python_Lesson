

print("""Faktöriyel bulan uygulama 
""")


while True : 
    istenen=input("faktöriyelini almak istediginiz sayıyı giriniz : ")
    fac=1
    if(istenen=="q"):
        print("Uygulama kapatılıyor")
        break
    else:
        istenen=int(istenen)
        if(istenen>=0):

            if(istenen==1 or istenen == 0 ):
                fac=1
                print("Factöriyeli istenen sayı = {} , Factöriyel sonucu = {} ".format(istenen,fac))
            else:
                for i in range(2,istenen+1):
                    fac*=i
                print("Factöriyeli istenen sayı = {} , Factöriyel sonucu = {} ".format(istenen,fac)) 
        else:
            print("Lütfen pozitif bir sayı giriniz")

    

