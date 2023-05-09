import requests
from bs4 import BeautifulSoup


# Code to input url
url = input("Enter ABC NEWS URL: ")
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
text = ''

for title in soup.find('title'):  # Retrieves title
    print(title.get_text())

for text in soup.find_all(class_="paragraph_paragraph__3Hrfa"):  # Returns body
    print(text.get_text())
