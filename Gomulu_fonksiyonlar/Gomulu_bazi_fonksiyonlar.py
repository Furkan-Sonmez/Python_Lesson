# -*- coding: utf-8 -*-

# map() fonksiyonu  : map(fonksiyon,iterasyon yapılabilicek veritipleri (liste vb ))



def double (x) :
    return x*2 

map (double , [1,2,3,4,5,6,7,8,9,])
print (list(map (double , [1,2,3,4,5,6,7,8,9,]))) # map tipindeki veriyi listeye çevirip yazdırdık 


liste1 = [1,2,3,4,5]
liste2 = [6,7,8,9,10]
liste3 = [11,12,13,14]

list (map (lambda x,y : x/y,liste1,liste2))

# reduce 

from functools import reduce 

def toplama (x,y): 
    return x+y 

print (reduce (toplama,[12,18,20,10])) # sırasıyla birbirine uygulattı aslında 12+18 = 30 sonra 30+20 = 50 sonra 50 + 10 = 60 şeklinde hesapladı 

reduce (lambda  x,y : x*y  , [1,2,3,4,5]) # 5 in faktoriyelini buldu aslında 

def maksimum (x,y): 
    if (x>y):
        return x 
    else : 
        return y 
print (reduce (maksimum , [1,2,3,4,5] ))

# filter fonksiyonu yapı olarak reduce ile aynı fakat boolen deger döner true veya false döndürün fonksiyon alır sadece 

print (list(filter (lambda x : x % 2 == 0,[1,2,3,4,5,6,7] )))  # sadece çift olanları dönücek mesela burda 

def asal_mi (x): 
    i = 2 
    if (x == 1 ):
        return False
    elif (x == 2 ):
        return True 
    else : 
        while (i < x ): 
            if (x % i == 0 ): 
                return False 
            i += 1 
            return True 
        
print (list (filter (asal_mi,range(1,100)))) 

# zip fonksiyonu gruplama yapmayı saglıyor liste1 [1,2,3,4,5] liste2[6,7,8,9,10,11] listelerini mesela 1 6 , 2 7 ,3 8 olucak şekilde gruplamamızı sağlıyor
liste1 = [1,2,3,4,5] 
liste2 = [6,7,8,9,10,11]
liste3 = ["Python","Php","Java","Javascript"]
print (list (zip(liste1 ,liste2,liste3)) )


# enumerate fonksiyonu 

liste = ["Elma","Armut","Muz","Kiraz"]
i = 0 
sonuc = list()
while (i < len (liste )): 
    sonuc.append((i,liste[i]))
    i += 1
print (sonuc) 


list (enumerate(liste)) # yukardaki işlemin kısa hali 

# kullana bilecek yerler
for i , j in enumerate(liste):
    print (i,j)
   
   
# all ve any fonksiyonları 

#all degerlerin hepsi true ise true döndürüyor diger şekilde her şekilde false döndürür
#any degerlerin herhangi biri true iste true hepsi yanlışsa false gönderir 




       