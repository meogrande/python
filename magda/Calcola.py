from Calcolatrice import *

def main():
    finito = False
    while not finito:
        ins = int(input("Vuoi fare una operazione? 1 sì, 2 no"))
        if ins ==2:
            finito = True
            print("Fine del programma")
        else:
            c = Calcolatrice()
            print("Inserisci il primo numero")
            c.setA(float(input()))
            print("Inserisci il secondo numero")
            c.setB(float(input()))
            print(c)
            print("\nScegli l'operazione da eseguire")
            print("1. Addizione")
            print("2. Sottrazione")
            print("3. Moltiplicazione")
            print("4. Divisione")
            scelta = int(input())
            if scelta == 1:
                print("\n" + str(c.addizione()))
            elif scelta == 2:
                print("\n" + str(c.sottrazione()))
            elif scelta == 3:
                print("\n" + str(c.moltiplicazione()))
            elif scelta == 4:
                print("\n" + str(c.divisione()))
            else:
                print("\nOperazione non valida")

main()

