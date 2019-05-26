#! python3

import requests, os, bs4

url = 'https://www.bizarro.com/pirates'

os.makedirs('bizarro', exist_ok=True)
print('Pobieranie strony %s....' % url)
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text)

comicElem = soup.select('img')
print(comicElem)
for comic in range(len(comicElem)):
    comicUrl = comicElem[comic].get('src')
    print('Pobieranie ' + str(comicUrl) + '...')
    try:
        res = requests.get(comicUrl)
        res.raise_for_status()
    except:
        pass
    try:
        imageFile = open(os.path.join('bizarro', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    except:
        pass





