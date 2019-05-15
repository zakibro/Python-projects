#!python3
#skrypt ściąga obrazki z imgur/ test "jimi cool"
import requests, os, bs4

url = 'https://imgur.com/search?q='

print('Co chceszy wyszukać na Imgur:')
search = input()

fullurl = url + search

res = requests.get(fullurl)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text)

elems = soup.select('a.image-list-link')
amount = len(elems)

list_of_images = []
images = soup.findAll('img')
for image in images:
    list_of_images.append(image['src'])

print(list_of_images)



counter = 1
for image in list_of_images:
    theUrl = 'https:' + image
    print(theUrl)
    res = requests.get(theUrl)
    res.raise_for_status()
    imageFile = open('image' + str(counter) + '.jpg', 'wb')
    for chunk in res.iter_content(10000):
        imageFile.write(chunk)
    imageFile.close()
    counter += 1

