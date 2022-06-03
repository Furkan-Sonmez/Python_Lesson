# -*- coding: utf-8 -*-



def anaFonksiyon (işlemAdı):
    def toplama (*args):
        toplam = 0 
        for i in args :
            toplam += i
        return toplam 
    def çarpım(*args):
        çarpım = 1 
        for i in args: 
            çarpım *= i 
        return çarpım 
    
    if işlemAdı =="toplama":
        return toplama
    else: 
        return çarpım
    
    

fonk = anaFonksiyon("toplama")
fonk(1,2,3,4,1)

fonk2 = anaFonksiyon("çarpım")
fonk2(12,3,2)    
  