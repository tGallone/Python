import requests, random
from bs4 import BeautifulSoup

channel = 'https://www.youtube.com/channel/UCwy3ZvkYjPZlusYo-CGIEcA/videos'
# r = requests.get('https://www.youtube.com/user/YouTube/videos', cookies={'CONSENT': 'PENDING+999'})

# r = requests.get('https://www.youtube.com/user/YouTube/videos', cookies={'CONSENT': 'YES+cb.20210328-17-p0.en-GB+FX+{}'.format(random.randint(100, 999))})
r = requests.get('https://www.youtube.com/channel/UCwy3ZvkYjPZlusYo-CGIEcA/videos', cookies=
                 {'CONSENT': 'YES+cb.20210328-17-p0.en-GB+FX+{}'.format(random.randint(100, 999))})

#r = requests.get(channel)
print(r)

soup = BeautifulSoup(r.content, 'html.parser')
#print(soup)
soup2 = soup.select_one('.yt-simple-endpoint style-scope ytd-grid-video-renderer')['title']
print(soup2)

# #'Final remarks and conference close  - Pycon 2017'