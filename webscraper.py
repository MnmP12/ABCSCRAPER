import PySimpleGUI as sg


def make_first_win():  # Function to create first window
    # Colour of first window
    sg.theme("DarkBrown5")
    # Contents of first window
    layout = [[sg.Text('Enter ABC News article here:'), sg.InputText()],
              [sg.Button('View')]]
    # Window creation
    return sg.Window("ABCSCRAPER", layout, finalize=True)


def make_second_win():  # Function to create second window
    # Colour of second window
    sg.theme("DarkBrown5")
    # Contents of second window 
    layout = [[sg.Text('This works')]]
    # Window creation
    return sg.Window("THISWORKS", layout, finalize=True)


window1, window2 = make_first_win(), None

while True:
    window, event, values = sg.read_all_windows()
    if event == sg.WIN_CLOSED:  # If 2nd window is open close, if 1st exit.
        window.close()
        if window == window2:
            window2 = None
        elif window == window1:
            break
    if event == 'View' and not window2:
        window2 = make_second_win()