import os
import re

#program szuka stringa w plikach w . folderze

print('Podaj wyraz który chcesz wyszukać:')
wyraz = input()

wyrazRegex = re.compile(wyraz)

listo = os.listdir()

for f in listo:
	if '.txt' in f:
		newfile = open(f, 'r')
		newfile = (newfile.read())
		mo = wyrazRegex.search(newfile)
		if mo == None:
			print('Nie ma takiego słowa w pliku ' + f)
		else:
			print('Słowo znajduje się w ' + f)
		
		
		
		
