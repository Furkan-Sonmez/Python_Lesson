
try : 
    file = open("bilgiler.txt","r",encoding="utf-8")   # read r si 
#birini seçenek
    for i in file : 
        print(i,end="") ## Burda virgülden sonra end "" demem yazmanın sonuna hi bişey koyma anlamına gelir normalde \n koyar 

# ikinci seçenek bunda ama 1 kere okunuyor çünkü 1 kere kullanınca imleci okudugu son yerde bıraktı 
    icerik = file.read()
    print(icerik)
# writeline var 3. seçenekte bu da tek satırı okumuş oluyoruz. 
# writelines bu da bir listeye yolluyor her satırı aşağıdaki gibi kullanılıyor
    liste = file.writelines()

except FileNotFoundError : 
    print("Dosya bulunamadı")
finally : 
    file.close()
    print("\ndosya kapandı")

