import PySimpleGUI as sg
import requests
from bs4 import BeautifulSoup


# Creates first window
def make_first_win():
    sg.theme("DarkBrown5")
    layout = [[sg.Text('Enter ABC News article URL:'), sg.InputText()],
              [sg.Button('View')]]
    return sg.Window("ABCSCRAPER", layout, finalize=True)


# Code to scrape ABC url in second window
def make_second_win(url):
    sg.theme("DarkBrown5")
    # Gathers source code
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    # Finds title/body text of page
    title_find = soup.find("title").get_text()
    infos = soup.find_all(class_="paragraph_paragraph__3Hrfa")
    body_find = "\n\n".join([info.get_text() for info in infos])
    # Initalizes measurements of window
    layout = [[sg.Text(title_find, size=(70, 0))],
              [sg.Multiline(body_find, size=(80, 30))]]
    return sg.Window("Article", layout, finalize=True)


# Ensures only first window opens when file is run
window1, window2 = make_first_win(), None

# While loop to close second window, exit program if first window is closed
while True:
    window, event, values = sg.read_all_windows()
    if event == sg.WIN_CLOSED:
        window.close()
        if window == window2:
            window2 = None
        elif window == window1:
            break
# If view is clicked, article is scraped in second window
    if event == 'View' and not window2:
        url = values[0]
        if url:
            window2 = make_second_win(url)
