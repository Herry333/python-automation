import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.lawlessrp.com/")
data = BeautifulSoup(response.text, 'html.parser')

links = data.find_all('a')  # Get all <a> tags

link_list = []  # Create a list to store links
for link in links:
    if 'href' in link.attrs:  #verify if te tag has "href" attribute
        link_list.append(link['href'])

print(link_list)
