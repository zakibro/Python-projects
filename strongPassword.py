
import re

print('Podaj hasło:')
text = input()

def eightChar(text):
	passwordRegex = re.compile(r'\w{8}')
	mo = passwordRegex.search(text)
	if mo == None:
		print('Hasło nie ma 8 znaków')
	else:
		print('Hasło ma 8 znaków')
		letters(text)

def letters(text):
	passwordRegex = re.compile(r'[A-Za-z]+')
	mo1 = passwordRegex.search(text)
	if mo1 != None:
		numbers(text)
	else:
		print('Słabe hasło')

def numbers(text):
	passwordRegex = re.compile(r'[0-9]+')
	mo2 = passwordRegex.search(text)
	if mo2 != None:
		print('Mocne hasło')
	else:
		print('Słabe hasło')
	
		
	
	

eightChar(text)
