# Web Scrapper

import requests
from bs4 import BeautifulSoup as bs
import os

# Website with Jim Harbaugh Images
url = 'https://gettyimages.com/photos/jim-harbaugh'

# Download Page for Parsing
page = requests.get(url)
soup = bs(page.text, 'html.parser')

# locate all elements with image tag
image_tags = soup.findAll('img')

# creates directory for Jim Harbaugh images
if not os.path.exists('jim_harbaugh'):
  os.makedirs('jim_harbaugh')

# move to new directory
os.chdir('jim_harbaugh')

# image file new variable
x = 0

# writing images
for image in image_tags:
  try:
    url = image['src']
    source = requests.get(url)
    if source.status_code == 200:
      with open('jim_harbaugh-' + str(x) + '.jpg', 'wb') as f:
        f.write(requests.get(url).content)
        f.close()
        x += 1
  except:
    pass
