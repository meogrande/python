# -*- coding: utf-8 -*-
print ("ciao mondo")
# questo è un commento
# attenzione alla formattazione
# coding: utf8
print(u"òàè+一二三四五".encode('utf-8'))
print (u'哈哈'.encode('utf-8'))
print (u'哇哈')
# ' vs ""
print ("ciao", 'ciao', " l'\"ha ", 'h"h')
# operazioni
print ("Divisione: ", 5 / 2)
print ("Divisione intera:", 5 // 2)
print ("Moltiplicazione: ", 5 * 2)
print ("Differenza: ", 5 - 2)
print ("Resto divisione: ", 5 % 2)
print ("Somma: ", 5 + 2)
print ("Elevamento a potenza: ", 5**2)

# variabili
i = int(5)
x = int(1)
# cicli
i = 1
while i < 6:
  print(i)
  i += 1
# for
print ("ciao")
for i in range(3):
        print(i)
for i in ['a',5,6]:
        print(i)
for i in range(5):
        for j in range(0,i):
                print(i, end='') # così non va a capo in automatico
        print() # manda a capo
# input: Ogni input di default è una stringa
# print ("Inserisci un numero maggiore di due")
#x = input("Inserisci un numero maggiore di due")
x = int(input("Inserisci un numero maggiore di due: "))
#print ("Hai inserito " + x + "!") + funziona solo con le stringhe
if (x*1 > 2):
    print ("Bravo")
else:
    print ("Eh no!")

# funzione per verificare se un numero è float
def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False


# Controllo di tipo
x = input("Inserisci qualcosa e ti dico il tipo: ")

print ("Hai inserito: ", x, "\n Ha solo cifre? " + " ", x.isdigit(), "\n Ha solo numeri (anche in altre lingue)? " , x.isnumeric(), "\n E' un numero con la virgola? ",isfloat(x), "!")

# Array
cars = ["Ford", "Volvo", "BMW"]
print(cars[0]) # Stampa il primo elemento
print (len(cars))