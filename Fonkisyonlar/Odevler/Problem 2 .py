
"""Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın."""

def ebob (sayı1 , sayı2):
    ebob = 1 
    for i in range (1, sayı1+sayı2):
        if (sayı1 % i == 0 and  sayı2 % i == 0 and i <= sayı1 and i <= sayı2 ):
            ebob*=i
    print ("{} ve {} sayılarının ebobu {}".format(sayı1 , sayı2 , ebob))

sayı1 = int (input())
sayı2 = int (input())
ebob(sayı1 , sayı2)
    





    