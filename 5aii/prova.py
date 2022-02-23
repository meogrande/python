# https://pysimplegui.readthedocs.io/en/latest/
import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# open file




# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()

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