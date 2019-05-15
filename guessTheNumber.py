
#Gra typu odgadnij liczbę

import random


#Sześć prób
def game():
	secrect_number = random.randint(1,20)

	print("Mam na myśli pewną liczbę z zakresu 1 do 20.")
	for guessTaken in range(1, 7):
		print("Spróbuj odgadnąć liczbę.")
		guess = int(input())
	
		if guess < secrect_number:
			print("Podana liczba jest za mała.")
		elif guess > secrect_number:
			print("Podana liczba jest za duża.")
		else:
			break

	if guess == secrect_number:
		print("Doskonale! Odgadłeś liczbę w ciągu " + str(guessTaken) + " prob.")
	else:
		print("Nie udało Ci się. Liczba, którą miałem na myśli to " + str(secrect_number) + ".")
	
	print("Czy chcesz zagrać jeszcze raz? (tak/nie)")
	answer = input()

	if answer == 'tak':
		game()
	else:
		print("Nareczka")

game()
	
