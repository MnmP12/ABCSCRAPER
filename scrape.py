import PySimpleGUI as sg
import requests
from bs4 import BeautifulSoup

# Function to create the main window
def make_first_win():
    sg.theme("DarkBrown5")
    layout = [[sg.Text('Top 5 Stories of the day:')]]
    
    # Add buttons labeled with numbers 1 to 5
    for i in range(1, 6):
        layout.append([sg.Button(str(i), key=f'button_{i}', size=(4, 1))])
    
    return sg.Window("ABCSCRAPER", layout, finalize=True, grab_anywhere=True)  # Make the window movable

# Main code
window1 = make_first_win()

while True:
    event, values = window1.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event.startswith('button_'):
        selected_index = int(event.split('_')[1])
        print(f"You pressed button {selected_index}")











