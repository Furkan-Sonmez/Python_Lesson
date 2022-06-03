# -*- coding: utf-8 -*-
import sqlite3 

con = sqlite3.connect("Şarkı.db") # kütüphane veritabanını oluşturucak ve bağlanıcak 
cursor = con.cursor()
cursor.execute("CREATE TABLE IF NOT  EXISTS Şarkı (Şarkı_İsmi TEXT,Sanatçı TEXT,Prodüksiyon_şirketi TEXT , Şarkı_süresi FLOAT)")
con.commit()


def süreToplam():
    
    sorgu = "Select Şarkı_süresi From Şarkı"
    cursor.execute(sorgu)
    liste =  cursor.fetchall() 
    sonuc = 0 
    for i in liste : 
        sonuc +=i[0] 
        
    return sonuc     

def sarkıEkle(Şarkı_İsmi,Sanatçı,Prodüksiyon_şirketi , Şarkı_süresi ): 
   
    cursor.execute("INSERT INTO Şarkı VALUES(?,?,?,?)",(Şarkı_İsmi,Sanatçı,Prodüksiyon_şirketi , Şarkı_süresi))
    con.commit()
    print ("şarkı eklendi")

def şarkıSil(isim): 
    cursor.execute("Delete From Şarkı where İsim = ? ",(isim,))
    con.commit()
    print("şarkı silindi")




print (süreToplam())


Şarkı_İsmi = input("eklemek istediginiz şarkının adını girin :")
Sanatçı = input("eklemek istediginiz Sanatçı adını girin :")
Prodüksiyon_şirketi = input("eklemek istediginiz Prodüksiyon_şirketi adını girin :")
Şarkı_süresi = float(input("eklemek istediginiz şarkının Şarkı_süresi girin :"))

sarkıEkle(Şarkı_İsmi, Sanatçı, Prodüksiyon_şirketi, Şarkı_süresi)



silinicek_şarkı = input("Silmek istediginiz şarkının adını girin :")   
şarkıSil(silinicek_şarkı)





con.close() 