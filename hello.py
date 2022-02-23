print("ciao mondo")

x = 9
print(x // 2) # Divisione intera
print("hai", x, "anni\n")
print("hai" + str(x) + "anni")
print(2**10)
parola = str("Ciao")
numero = int(12.4)
print(numero)
if numero < 20:
    print("Minore di 20")
    print("asa")
else: 
    print("Maggiore di 20")
if numero < 10:
    print("cada")
i = 0
while i < 5:
    print(i)
    i += 1
    print('ciao')

for i in range(5,12,2): # utilizzo di range
    print(i)

for i in ['Austria','Croazia','Piave','Montagna',"Jesolo"]:
    print(i)

for i in range(4):
    for j in range(4):
        print(i*j, end='')
    print()

print("Inserisci un numero e ti stampo il quadrato")
parola = input()
try: # Provate a mettere il codice in un ciclo: si esce se il numero è valido
    n = int(parola)
    print("Il quadrato è: ", n**2)
except ValueError:
    print(ValueError)
    print("Non posso calcolare il quadrato")

def funzione(valore):
    return valore + 8

print(funzione(5))

prova = ["w","d","e"]
print(len(prova))
print(prova[2])
for i in prova:
    print(i)
