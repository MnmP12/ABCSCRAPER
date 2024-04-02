import PySimpleGUI as sg
import requests
from bs4 import BeautifulSoup

# Function to create the main window
def make_first_win():
    sg.theme("DarkBrown5")
    layout = [[sg.Text('Top 5 ABC articles today:', size=(20, 1), justification='center')]]
    
    # Add buttons labeled with numbers 1 to 5
    button_layout = [[sg.Button(str(i), key=f'button_{i}', size=(4, 1), pad=(2, 2), button_color=('white', sg.theme_background_color()))] for i in range(1, 6)]
    layout.append([sg.Column(button_layout, element_justification='center', vertical_alignment='center')])
    
    return sg.Window("ABCSCRAPER", layout, finalize=True, grab_anywhere=True, size=(200, 200))  # Make the window movable

# Main code
window1 = make_first_win()

while True:
    event, values = window1.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event.startswith('button_'):
        selected_index = int(event.split('_')[1])
        print(f"You pressed button {selected_index}")













