#! python3
#luckyGoogle szuka w google
#sys.argv jako słowo klucz do wyszukania
#program "klika" w pięc pierwszych linków z Google

import requests, sys, webbrowser, bs4

print('Szukam.')
res = requests.get('https://www.google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text)

linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('https://www.google.com' + linkElems[i].get('href'))
