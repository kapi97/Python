import sys
import math

def dodawanie(a, b):
	c = a + b
	return c

def odejmowanie(a, b):
	c = a - b
	return c

def mnozenie(a, b):
	c = a * b
	return c

def dzielenie(a, b):
        if b != 0:
                c = a / b
                return c
        else:
                print ("Nie dziel przez zero!")
                return 0

def modulo(a, b):
        c = math.fmod(a, b)
        return c

def potegowanie(a, b):
	c = math.pow(a, b)
	return c

def pot_kw(a):
        b = 2
        c = a ** b
        return c

def pot_sz(a):
        b = 3
        c = a ** b
        return c

def pierwiastkowanie(a):
	c = math.sqrt(a)
	return c

def procent(a):
        b = 100
        c = a / b
        return c

def logarytm_dec(a):
        c = math.log10(a)
        return c

def logarytm_nat(a):
        c = math.log(a)
        return c

def silnia(a):
        c = math.factorial(a)
        return c

def silnia_rek(a):
        if a > 1:
                return a * silnia(a - 1)
        elif a in (0,1):
                return 1

def w_bezw(a):
        c = math.fabs(a)
        return c

def sin(a):
        c = math.sin(a)
        return c

def cos(a):
        c = math.cos(a)
        return c

def tan(a):
        c = math.tan(a)
        return c

def pi():
        c = math.pi
        return c

def e():
        c = math.e
        return c

def zlyWybor():
	print("Dokonales zlego wyboru!")
	sys.exit()

wyjscie = False
while wyjscie == False:

        print("\nWitamy w programie 'Kalkulator'\nINFORMACJA: dzialania od 1 do 6 wymagaja podania 2 liczb, dzialania od 7 do 16 tylko jednej na poczatek i potem podac 0, ostatnie dwa dzialania sa to liczby stale - wystarczy podac zera\n")
        a = int(input("Podaj pierwsza liczbe - jesli nie, podaj 0: "))
        b = int(input("Podaj druga liczbe - jesli nie, podaj 0: "))
        c = input("\nWybierz rodzaj dzialania: 1 - dodawanie, 2 - odejmowanie, 3 - mnozenie, 4 - dzielenie, 5 - modulo, 6 - potegowanie, 7 - potegowanie kwadratowe, 8 - potegowanie szescienne, 9 - pierwiastkowanie, 10 - procentowanie, 11 - logarytm dziesietny, 12 - logarytm naturalny, 13 i 14 - silnia, 15 - wartosc bezwzgledna, 16 - sin, 17 - cos, 18 - tan, 19 - pi, 20 - e: \n")
        if (c == '1'):
                wynik = dodawanie(a, b)
        elif (c == '2'):
                wynik = odejmowanie(a, b)
        elif (c == '3'):
                wynik = mnozenie(a, b)
        elif (c == '4'):
                wynik = dzielenie(a, b)
        elif (c == '5'):
                wynik = modulo(a, b)
        elif (c == '6'):
                wynik = potegowanie(a, b)
        elif (c == '7'):
                wynik = pot_kw(a)
        elif (c == '8'):
                wynik = pot_sz(a)
        elif (c == '9'):
                wynik = pierwiastkowanie(a)
        elif (c == '10'):
                wynik = procent(a)
        elif (c == '11'):
                wynik = logarytm_dec(a)
        elif (c == '12'):
                wynik = logarytm_nat(a)
        elif (c == '13'):
                wynik = silnia(a)
        elif (c == '14'):
                wynik = silnia_rek(a)
        elif (c == '15'):
                wynik = w_bezw(a)
        elif (c == '16'):
                wynik = sin(a)
        elif (c == '17'):
                wynik = cos(a)
        elif (c == '18'):
                wynik = tan(a)
        elif (c == '19'):
                wynik = pi()
        elif (c == '20'):
                wynik = e()
        else:
                zlyWybor()

        print("Wynik: ", wynik)

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
