
print("""
Fibonaçi serisini bulan uygulamaya goşgeldiniz 
""")

while True:
    sırala=input ("Uygulamadan çıkmak için q ya basın . Kaçıncı sıraya kadar yazılmasını istedigini giriniz : ")
    if(sırala=="q"):
        print("Uygulamadan çıkılıyor")
        break 
    else:
        sırala=int(sırala)
        if(sırala>=0):
            a=1 
            b=1
            fib=[a,b]
            for i in range(sırala-2):
                a,b=b,a+b
                fib.append(b)
                    
            print(fib,sep = "-")
            
           
        else:
            print ("Girdiginiz sayı negatif lütfen pozitif bi sayı giriniz")
         
            
