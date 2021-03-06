# hello_psg.py
# https://pysimplegui.readthedocs.io/en/latest/cookbook/

import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [[sg.Text("Saluti da PySimpleGUI")], [sg.InputText("Inserisci qualcosa",key="-pippo-")], [sg.Button("OK")]] 

# Create the window
window = sg.Window("Prima prova", layout)
    

# Create an event loop
while True:
    event, values = window.read()
    text_input = values["-pippo-"]    
    sg.popup('Hai scritto:', text_input)
    window["-pippo-"].update("mamma")
    # End program if user closes window or
    # presses the OK button
    # if event == "OK" or event == sg.WIN_CLOSED:
    if event == sg.WIN_CLOSED:
        break

window.close()
