import requests
from requests_html import HTMLSession 
from bs4 import BeautifulSoup as bs # importing BeautifulSoup

# sample youtube video url
video_url = "https://www.youtube.com/watch?v=jNQXAC9IVRw"
# init an HTML Session
session = HTMLSession()
# get the html content
response = session.get(video_url)
# execute Java-script
response.html.render(sleep=1)
# create bs object to parse HTML
soup = bs(response.html.html, "html.parser")
# write all HTML code into a file
open("video.html", "w", encoding='utf8').write(response.html.html)