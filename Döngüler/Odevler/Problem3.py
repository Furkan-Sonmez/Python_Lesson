
print("""
Çarpım tablosu""")

while True:
    print ("""Hangi sayıdan hangi sayıya kadar çarpım tablosu görmek istediginizi yazın""")
    baslangıc =int (input ("""Hangi sayıya kadar çarpım tablosunu görmek istiyorsunuz :  """))
    bitiş=int (input ("Çarpımlar hangi sayıya kadar olsun :  "))

    for i in range(baslangıc+1):
        print("**************")
        for j in range (bitiş+1):
            çarpım=i*j
            print ("{} x {} = {}".format(i,j,çarpım))
            
    a=input ("uygulamayı durdurmak için q ya basınız  devam etmek için herhangi bir tuşa basın: ")
    if(a=="q"):
        break 
     
        
