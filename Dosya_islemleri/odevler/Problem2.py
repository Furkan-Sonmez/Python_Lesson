# -*- coding: utf-8 -*-

with open("Şiir.txt","r",encoding="utf-8") as file :
    
    dosya_okuma = file.read()
    cumleler = list(dosya_okuma.split("\n"))
    for i in range (0 ,len(cumleler)):
        print (cumleler[i][0])
    