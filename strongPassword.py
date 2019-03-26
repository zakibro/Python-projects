
import re

print('Type Password:')
text = input()

def eightChar(text):
	passwordRegex = re.compile(r'\w{8}')
	mo = passwordRegex.search(text)
	if mo == None:
		print("Password hasn't got 8 charactes")
	else:
		print("Password has got 8 characters")
		letters(text)

def letters(text):
	passwordRegex = re.compile(r'[A-Za-z]+')
	mo1 = passwordRegex.search(text)
	if mo1 != None:
		numbers(text)
	else:
		print('Weak password')

def numbers(text):
	passwordRegex = re.compile(r'[0-9]+')
	mo2 = passwordRegex.search(text)
	if mo2 != None:
		print('Strong password')
	else:
		print('Weak password')
	
		
	
	

eightChar(text)
