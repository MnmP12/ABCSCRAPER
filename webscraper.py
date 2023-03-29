import requests
from bs4 import BeautifulSoup

url = input("Enter ABC NEWS URL: ")  # Prints the instructions to CMD
html_source = requests.get(url)
soup = BeautifulSoup(html_source.content, 'html5lib')
text = ''

for title in soup.find_all('title'):  # This line of code retrieves the article
    print(title.get_text())

for text in soup.find_all(class_='_39n3n'):  # This returns the content
    print(text.get_text())
