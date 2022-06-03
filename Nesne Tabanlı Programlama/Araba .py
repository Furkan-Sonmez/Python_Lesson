class araba () : 
    def __init__(self,model="Bilgi yok",renk="Bilgi yok",hp="Bilgi yok",silindir="Bilgi yok"):
        self.model = model 
        self.renk = renk 
        self.hp = hp 
        self.silindir = silindir


araba1 = araba("renault","gümüş", silindir = "4")    
araba2 = araba("bmw","gümüş", "400","8")   


print(araba1.hp)