# -*- coding: utf-8 -*-

import sqlite3 

con = sqlite3.connect("kütüphane.db") # kütüphane veritabanını oluşturucak ve bağlanıcak 
cursor = con.cursor()


# kitaplık tablosu oluşturma 

def tablo_olustur(): 
    cursor.execute("CREATE TABLE IF NOT  EXISTS kitaplık (İsim TEXT,Yazar TEXT,Yayınevi TEXT , Sayfa_sayisi INT)")
    con.commit()

# veri eklemeler
def veri_ekle():
    cursor.execute("INSERT INTO kitaplık VALUES('İSTANBUL HATIRASI ', 'AHMET ÜMİT','EVERST YAYINCILIK',561)")
    con.commit()


def veri_ekle2(isim,yazar,yayınEvi,sayfaSayısı): 
    cursor.execute("INSERT INTO kitaplık VALUES(?,?,?,?)",(isim,yazar,yayınEvi,sayfaSayısı))
    con.commit()
    
# veri çekmeler 

"""
Select*From kitaplık tablodaki tüm bilgileri almamızı sağlar 
Select İsim,Yazar From kitaplık tablodaki tüm bilgilerin sadece isim ve yazar özelliklerini almamızı saglar 
Select*from kitaplık where Yayınevi = 'Everest' sadece yayınevi özelliği everest olanları alır 
"""

def verileri_al(): 
    cursor.execute("Select  * From kitaplık")
    liste = cursor.fetchall()
    print("kitaplık tablosunun bilgileri")
    for i in liste:
        print(i)
        
def verileri_al2(): 
    cursor.execute("Select İsim,Yazar From kitaplık")    
    liste = cursor.fetchall()
    print("kitaplık tablosunun bilgileri")
    for i in liste:
        print(i)
        
    
    
def verileri_al3(isim): 
    cursor.execute("Select * From kitaplık where İsim = ?",(isim,))    
    liste = cursor.fetchall()
    print("kitaplık tablosunun bilgileri")
    print("3. fonksiyon çalıştı")
    for i in liste:
        print(i)
    
    
    
# verileri güncellemek 

def verilerigüncelle(eskiYayınevi,yeniYayınevi):
    cursor.execute("Update kitaplık set Yayınevi = ?  where Yayınevi = ? ",(yeniYayınevi,eskiYayınevi))  
    con.commit()
    
# verileri silmek 
def verilerisil(isim): 
    cursor.execute("Delete From kitaplık where İsim = ? ",(isim,))
    con.commit()


    
isim = input("İsim:")
yazar = input("Yazar:")
yayınEvi = input("Yayınevi:")
sayfaSayısı = int(input("Sayfa sayısı:"))


tablo_olustur()

veri_ekle()     
veri_ekle2(isim,yazar,yayınEvi,sayfaSayısı)

verileri_al()  
verileri_al2()   
verileri_al3("furkan")

verilerigüncelle("EVERST YAYINCILIK","değişen")
print("degğişmiş tablo")
verileri_al() 


verilerisil("furkan")
print("degğişmiş tablo")
verileri_al() 

con.close() # dosyalarda ki gibi bunu da kapatılıyor 




 
