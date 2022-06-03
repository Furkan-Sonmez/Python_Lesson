# -*- coding: utf-8 -*-



## Dosaya işlemlerini burda yapıyoruz ve bu bitince dosya direk kapanmış oluyor daha fazla uğraşmamış oluyoruz 
with  open ("bilgiler.txt","r",encoding = "utf-8") as file : 
    for i in file : 
        print (i)


## dosyalarda geri sarma 

with  open ("bilgiler.txt","r",encoding = "utf-8") as file : 
    for i in file : 
        print (file.tell())
        file.seek(20)
        print (file.tell())
        ## tell () dosya degişkeninin nerde oldugunu söylüyor dosyanın içinde kaçıncı byt 
        

## dosyanın 5. byt a gidiyoruz ordan okumaya çalışıyoruz aşagıda
with  open ("bilgiler.txt","r",encoding = "utf-8") as file : 
    for i in file : 
        file.seek(5)
        icerik = file.read(10) ##10 byt okuycak 
        print (icerik)
        
        
        
        