import os
from os.path import join

szukanyPlik = input("Podaj nazwe pliku, ktorego szukasz: ")
sciezka = input("Podaj sciezke, gdzie chcesz szukac pliku: ")

for root, dirs, files in os.walk(sciezka):
	print ("Szukam:", root)
	if szukanyPlik in files:
		print ("PLIK ZNALEZIONY: %s" % join(root, szukanyPlik))
		break
