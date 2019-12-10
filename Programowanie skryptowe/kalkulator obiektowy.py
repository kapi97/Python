import sys
import math

class Kalkulator:

	def __init__(self, a, b):
		self.a = a
		self.b = b

	def __del__(self):
		del self.a
		del self.b

	def dodawanie(self):
		return self.a + self.b

	def odejmowanie(self):
		return self.a - self.b

	def mnozenie(self):
		return self.a * self.b

	def dzielenie(self):
		if self.b != 0:
			return a / b
		else:
			print ("Nie dziel przez zero!")
			return 0

	def modulo(self):
		return math.fmod(self.a, self.b)

	def potegowanie(self):
		return math.pow(self.a, self.b)

	def pot_kw(self):
		self.b = 2
		return self.a ** self.b

	def pot_sz(self):
		self.b = 3
		return self.a ** self.b

	def pierwiastkowanie(self):
		return math.sqrt(self.a)

	def procent(self):
		self.b = 100
		return self.a / self.b

	def logarytm_dec(self):
		return math.log10(self.a)

	def logarytm_nat(self):
		return math.log(self.a)

	def silnia(self):
		return math.factorial(self.a)

	def silnia_rek(self):
		if self.a > 1:
			return self.a * silnia(self.a - 1)
		elif self.a in (0,1):
			return 1

	def w_bezw(self):
		return math.fabs(self.a)

	def sin(self):
		return math.sin(self.a)

	def cos(self):
		return math.cos(self.a)

	def tan(self):
		return math.tan(self.a)

	def pi(self):
		return math.pi

	def e(self):
		return math.e

	def wyswietlWynik(self, wynik):
		print ("Wynik: ", wynik)

def zlyWybor():
        print("Dokonales zlego wyboru!")
        sys.exit()

wyjscie = False
while wyjscie == False:

        print("\nWitamy w programie 'Kalkulator'\nINFORMACJA: dzialania od 1 do 6 wymagaja podania 2 liczb, dzialania od 7 do 16 tylko jednej na poczatek i potem podac 0, ostatnie dwa dzialania sa to liczby stale - wystarczy podac zera\n")
        a = int(input("Podaj pierwsza liczbe - jesli nie, podaj 0: "))
        b = int(input("Podaj druga liczbe - jesli nie, podaj 0: "))
        kalkulator = Kalkulator(a, b)

        c = input("\nWybierz rodzaj dzialania: 1 - dodawanie, 2 - odejmowanie, 3 - mnozenie, 4 - dzielenie, 5 - modulo, 6 - potegowanie, 7 - potegowanie kwadratowe, 8 - potegowanie szescienne, 9 - pierwiastkowanie, 10 - procentowanie, 11 - logarytm dziesietny, 12 - logarytm naturalny, 13 i 14 - silnia, 15 - wartosc bezwzgledna, 16 - sin, 17 - cos, 18 - tan, 19 - pi, 20 - e: \n")

        if (c == '1'):
                wynik = kalkulator.dodawanie()
                kalkulator.wyswietlWynik(wynik)
        elif (c == '2'):
                wynik = kalkulator.odejmowanie()
                kalkulator.wyswietlWynik(wynik)
        elif (c == '3'):
                wynik = kalkulator.mnozenie()
                kalkulator.wyswietlWynik(wynik)
        elif (c == '4'):
                wynik = kalkulator.dzielenie()
                kalkulator.wyswietlWynik(wynik)
        elif (c == '5'):
                wynik = kalkulator.modulo()
                kalkulator.wyswietlWynik(wynik)
        elif (c == '6'):
                wynik = kalkulator.potegowanie()
                kalkulator.wyswietlWynik(wynik)
        elif (c == '7'):
                wynik = kalkulator.pot_kw()
                kalkulator.wyswietlWynik(wynik)
        elif (c == '8'):
                wynik = kalkulator.pot_sz()
                kalkulator.wyswietlWynik(wynik)
        elif (c == '9'):
                wynik = kalkulator.pierwiastkowanie()
                kalkulator.wyswietlWynik(wynik)
        elif (c == '10'):
                wynik = kalkulator.procent()
                kalkulator.wyswietlWynik(wynik)
        elif (c == '11'):
                wynik = kalkulator.logarytm_dec()
                kalkulator.wyswietlWynik(wynik)
        elif (c == '12'):
                wynik = kalkulator.logarytm_nat()
                kalkulator.wyswietlWynik(wynik)
        elif (c == '13'):
                wynik = kalkulator.silnia()
                kalkulator.wyswietlWynik(wynik)
        elif (c == '14'):
                wynik = kalkulator.silnia_rek()
                kalkulator.wyswietlWynik(wynik)
        elif (c == '15'):
                wynik = kalkulator.w_bezw()
                kalkulator.wyswietlWynik(wynik)
        elif (c == '16'):
                wynik = kalkulator.sin()
                kalkulator.wyswietlWynik(wynik)
        elif (c == '17'):
                wynik = kalkulator.cos()
                kalkulator.wyswietlWynik(wynik)
        elif (c == '18'):
                wynik = kalkulator.tan()
                kalkulator.wyswietlWynik(wynik)
        elif (c == '19'):
                wynik = kalkulator.pi()
                kalkulator.wyswietlWynik(wynik)
        elif (c == '20'):
                wynik = kalkulator.e()
                kalkulator.wyswietlWynik(wynik)
        else:
                zlyWybor()

        del kalkulator

        while True:
                pytanie = input("\nWyjsc z programu? (t/n): ")
                if pytanie == 't':
                        wyjscie = True
                        break
                elif pytanie == 'n':
                        break
                else:
                        print("Podales bledna litere!")

print("Koniec programu")
