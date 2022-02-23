class Calcolatrice(object):

    #Costruttore privo di parametri in ingresso
    def __init__(self):
        # __ permette di rendere gli attributi privati
        self.__a=0
        self.__b=0

    # i metodi delle classi sono contraddistinti dall'uso del self
    #SETTER
    def setA(self,a):
        self.__a=a

    def setB(self,b):
        self.__b=b
    #GETTER
    def getA(self):
        return self.__a

    def getB(self):
        return self.__b

    #Equivalente del TO STRING
    def __str__(self):
        return "Valore di a: " + str(self.__a) + "Valore di b: " + str(self.__b)

    #Altri metodi
    def addizione(self):
        return self.__a + self.__b

    def sottrazione(self):
        return self.__a - self.__b

    def moltiplicazione(self):
        return self.__a * self.__b

    def divisione(self):
        if self.__b == 0:
            print("\nDivided by Zero")
            #None equivale al NULL
            risultato=None
        else:
            risultato = self.__a / self.__b

        return risultato