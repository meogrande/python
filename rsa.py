
def mcd(a, b): # Eulero autogenerato! Pazzesco
    while b != 0:
        a, b = b, a % b
    return a

# Calcola il fi del numero
def fi(value):
    number = 0
    for i in range(1,value):
        if mcd(value,i) == 1:
            number += 1
    return number 
    
s = 7
m = 3
print (mcd(s,fi(m)))