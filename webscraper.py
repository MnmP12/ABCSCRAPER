import requests
from pprint import pprint
from bs4 import BeautifulSoup
import PySimpleGUI as sg

sg.theme("DarkBrown5")  # Colour of window
# Contents of window
layout = [[sg.Text('Enter ABC news article here:'), sg.InputText()],
          [sg.Button('View')]]
# Window creation
window = sg.Window('ABCSCRAPER', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:  # if user closes window 
        break
    
