# -*- coding: utf-8 -*-


def alan_hesapla (demet): 
    return demet[0] * demet[1]
dikdortgen_kenarlar = [(3,4),(10,3),(5,6),(1,9)]

print (list (map(alan_hesapla , dikdortgen_kenarlar)) )
