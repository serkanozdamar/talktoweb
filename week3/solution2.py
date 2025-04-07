# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = input('Enter count: ')
position = input('Enter position: ')
# count = 7
# position = 18

def get_tag_at_position(url, position):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')

    if position < len(tags) - 1:
        return tags[position-1].get("href", None)
    else:
        return None

# url = "http://py4e-data.dr-chuck.net/known_by_Karl.html"

last_name = None
for i in range(count):
    new_url = get_tag_at_position(url, position)
    if new_url:
        url = new_url
        last_name = new_url.split("/")[-1].replace("known_by_", "").replace(".html", "")

print(last_name)
