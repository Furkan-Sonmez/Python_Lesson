# -*- coding: utf-8 -*-

def fonksiyon(*args):
    for i in args : 
        print(i)
        
        
fonksiyon(1,2,3,4,5,12,3)


def fonskiyon2(isim,*args):
    print ("isim:",isim)
    
    print("--------------------")
    
    for i in args :
        print (i)
        
fonskiyon2( "furkan " , 1,2,123,123,123,43,4,3,"denem")        
    

def fonksiyon3(**kwargs):
    for i , j in kwargs.items():
        print("Argüman İsmi", i , "argüman değeri",j)
    
    
fonksiyon3(isim ="Murat",soyisim = "coşkun",numara=12314)   