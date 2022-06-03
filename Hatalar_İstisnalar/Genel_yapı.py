
try :
    a = int (input("Sayı1:"))
    b = int (input("Sayı2:"))
    print(a/b)
except ValueError :
    print ("Lütfen inputu doğru girin")
except ZeroDivisionError : 
    print("Bir sayi sıfır'a bölünemez")
finally : 
    print("Bu blok kesin çalışıyor ne olursa olsun.")

print("Bloklar sona erdi...")    

def terscevir (s): 
    if (type(s) != str):
        raise ValueError ("lütfen string bir değer göderin. print(terscevir(112)) den dolayı hata adık ve buraya türkçe istedigimizi yaza bildik ")
    else :
        return s[::-1]
print(terscevir(112))

try : 
    print (terscevir(12))
except ValueError :
    print("Fonksiyon valueerror hatası verdi")

