# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 15:08:57 2021

@author: furki
"""

def fonksiyon(*args):
    def toplama(args):
        toplam = 0 
        for i in args :
            toplam += i
        return toplam
    print(toplama(args))
    
    
fonksiyon(1,23,312,4,2,1,2,7)    

