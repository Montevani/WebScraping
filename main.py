import requests
from bs4 import BeautifulSoup as sp

user = input('Input Github User: ')
url = 'https://github.com/'+user
r = requests.get(url)
soup = sp(r.content, 'html.parser')
profile_image = soup.find('img', {'alt': 'Avatar'})['src']
print(profile_image)