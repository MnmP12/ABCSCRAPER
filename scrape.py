import requests
from bs4 import BeautifulSoup


# Accessing source code/gathering elements of html page
url = input("Enter ABC NEWS URL: ")
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
text = ''

# Retrieves title of article 
for title in soup.find('title'):  
    print(title.get_text())

# Returns body of article
for text in soup.find_all(class_="paragraph_paragraph__3Hrfa"):  
    print(text.get_text())
