import requests
from bs4 import BeautifulSoup

url = input("Enter ABC NEWS URL here : ")  #Add any abc news article link here.
html_source = requests.get(url)         #Retrieving abc news links source code.

soup = BeautifulSoup(html_source.content, 'html5lib')    # Gathering elements within the link.
for title in soup.find_all('title'):           
    print(title.get_text())
#Extracts Title of article.

text = ''
for text in soup.find_all(class_='_39n3n'):
    print(text.get_text()) 
#Extracts Content of article.                   

