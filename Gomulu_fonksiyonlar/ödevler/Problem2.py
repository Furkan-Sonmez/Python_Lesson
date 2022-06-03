# -*- coding: utf-8 -*-

def ucgen_mi (demet) : 
    if (abs(demet[1]-demet[2]) < demet [0] < demet[1]+demet[2]): 
        return True 
    elif (abs(demet[0]-demet[2]) < demet [1] < demet[0]+demet[2]): 
        return True  
    elif (abs(demet[0]-demet[1]) < demet [2] < demet[0]+demet[1]): 
        return True  
    else :
        return False 
    
Kenarlar = [(3,4,5),(6,8,10),(3,10,7)]   

print (list (filter (ucgen_mi , Kenarlar)))