import PySimpleGUI as sg
import requests 
from bs4 import BeautifulSoup
import webbrowser

url = "https://abcnews.go.com/"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

def scrape_article(url):
    article = ""
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        paragraphs = soup.find_all("p")
        for p in paragraphs:
            article += p.text.strip() + "\n"
    except Exception as e:
        print("Error:", e)
    return article

def scrape_headline(index):
    headline = ""
    url = ""
    header_ones = soup.select("h2.subNav__text")
    if index < len(header_ones):
        headline = header_ones[index].text.strip()
        # Find the link to the full article
        link_tag = header_ones[index].find_parent("a")
        if link_tag and "href" in link_tag.attrs:
            url = link_tag["href"]
    return headline, url

def generate_summary(article):
    max_length = 200  # Adjust the maximum length of the summary as needed
    if len(article) <= max_length:
        return article
    else:
        return article[:max_length] + "..."

def open_full_article(url):
    webbrowser.open_new_tab(url)

def make_first_win():
    sg.theme("DarkBrown5")
    layout = [[sg.Text('Top 7 ABC articles today:', size=(40, 1), justification='center',)]]
    
    button_layout = []
    for i in range(1, 8):
        headline, url = scrape_headline(i - 1)
        button_text = f'Article {i}: {headline}'
        button_layout.append([sg.Button(button_text, key=f'button_{i}', size=(40, 1), pad=(2, 2), button_color=('white', sg.theme_background_color()))])
        
    
    layout.append([sg.Column(button_layout, element_justification='center', vertical_alignment='center')])
    
    return sg.Window("ABCSCRAPER", layout, finalize=True, grab_anywhere=True, size=(400, 260))

window1 = make_first_win()

while True:
    event, values = window1.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event.startswith('button_'):
        selected_index = int(event.split('_')[1]) - 1  # Adjust index to start from 0
        headline, url = scrape_headline(selected_index)
        article = scrape_article(url)
        summary = generate_summary(article)
        new_layout = [[sg.Text(headline)], [sg.Text(summary)], [sg.Button('Read Full Article', key=f'link_{selected_index+1}')]]
        new_window = sg.Window(f'Article {selected_index+1}', new_layout, finalize=True)
        while True:
            event, values = new_window.read()
            if event == sg.WINDOW_CLOSED:
                new_window.close()
                break
            elif event.startswith('link_'):
                open_full_article(url)
