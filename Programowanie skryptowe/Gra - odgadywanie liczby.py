import random

print("Odgadywanie liczby od 1 do 100")
szukanaLiczba = random.randrange(1, 100)
strzal = 0
while strzal != szukanaLiczba:
	strzal = int(input("Odgadnij szukana liczbe:"))
	if (strzal < szukanaLiczba):
		print("Za mala!")
		continue
	elif (strzal > szukanaLiczba):
		print("Za duza!")
		continue
	print("Ostatnie wykonanie petli.")
print("Brawo, wygrales!")
