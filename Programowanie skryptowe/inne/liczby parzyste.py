print("Program dodajacy tylko liczby parzyste.")
wynik = 0
while wynik < 100:
	liczba = int(input("Podaj kolejna liczbe dodatnia: "))
	if (liczba < 0):
		print("Liczba musi byc dodatnia!")
		break;
	if (liczba % 2 == 0):
		wynik += liczba
	else:
		continue
print(wynik)
