# -*- coding: utf-8 -*-

class Dosya() :
    def __init__(self):
        
        with open ("metin.txt","r",encoding = "utf-8") as file :
            
            dosya_icerigi = file.read()
            
            kelimeler = dosya_icerigi.split() # kelimeleri boşluga göre ayırmış olduk her bir kelimeyi tek tek almış olduk yani 
            
            self.sade_kelimeler = list ()
            
            for i in kelimeler :    # kelimelerden parantez içinde yazanları çıkarttık 
                i = i.strip("\n")
                i = i.strip(" ")
                i = i.strip (".")
                i = i.strip (",")
                self.sade_kelimeler.append(i)
            
    def tum_kelimeler(self) : 
        kelimeler_kumesi = set() 
        for i in self.sade_kelimeler:
            kelimeler_kumesi.add(i)
            
        for i in kelimeler_kumesi:
            print (i)
            print("**************************")
        
    def kelime_frekansi(self):
       
       kelime_sozluk = dict()
       
       for i in self.sade_kelimeler:
           if (i in kelime_sozluk):
               kelime_sozluk[i] += 1 
           else:
               kelime_sozluk[i] = 1 
            
       for kelime,sayı in kelime_sozluk.items():
           print("{} kelime {} defa geçiyor ....".format(kelime , sayı))
           print("----------------------------------------------------")
        
        
dosya = Dosya()
dosya.kelime_frekansi()        