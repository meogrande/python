import PySimpleGUI as sg
sg.theme('DarkAmber')
layout = [[sg.Text("Ciao")],[sg.InputText()],[sg.Button("Ok")]]

window = sg.Window("Prova", layout)

window.read()


print("你好 mondo")
print("你好 mondo")
print("你好 mondo")
print("你好 mondo")

def mioinput(value):
    ok = False
    x = 0
    while not ok:
        try:
            x = input(value)
            x = int(x)
            ok = True
        except:
            pass
    return x


'''print("ciao","mondo")
print("ciao" + "mondo")'''
print(5/4) #divisione
print(5//4) #divisione intera
print(5%4) #resto
print(5**4) # potenza
#variabili
pippo = '''print("ciao","mondo")
print("ciao" + "mondo")'''
print(pippo)
print(type(pippo)) # stampa il tipo della variabile
x = int(1)
# ciclo
while x < 10:
    print(x)
    x += 1
#while True:
#    print("fermatemi!!!",end="\n")
# for
for i in range(3):
    print (i)
for i in range(3,8):
    print (i)
for i in range(3,8,2): #va da 3 a 8 saltando di due in due
    print (i)
for i in ["disa","de stefani",7]:
    print(str(i) + " " + str(type(i)))
# if
if 1 < 5 and 1 < 6:
    print("lo sapevo")
else:
    print("eh no")
# input
x = mioinput("Inserisci un numero: ")
print ("Hai inserito:",x, type(x))
if x > 6:
    print("più grande di sei")

#Array
cars=["ferrari","alfa","toyota"]
cars[2]="pippo"
for i in cars:
    print(i)
print(cars[0])
print(len(cars))

print("fine")