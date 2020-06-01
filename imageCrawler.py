# from google_images_download import google_images_download

# response = google_images_download.googleimagesdownload()

# arguments = {"keywords":"cat", "limit":20,"print_urls":True, "output_directory":"catcat", "format":"jpg"}

# paths = response.download(arguments)

# print(paths)

import os
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.parse import quote_plus

baseUrl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
plusUrl = input('어떤 이미지? : ')
# 한글 검색 자동 변환
url = baseUrl + quote_plus(plusUrl)
html = urlopen(url)
soup = bs(html, "html.parser")
img = soup.find_all(class_='_img', limit=50)

n = 1

os.mkdir('./img/'+plusUrl)
for i in img:
    imgUrl = i['data-source']
    with urlopen(imgUrl) as f:
        with open('./img/'+ plusUrl + '/' + plusUrl +str(n)+'.jpg','wb') as h:
            img = f.read()
            h.write(img)
    n += 1
print('다운로드 완료')
