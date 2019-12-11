plik = open("plik.txt", "w")
plik.write("Ala ma kota.")
plik.close()

plik = open("plik.txt", "r+")
zawartosc = plik.read()
print(zawartosc)

nowaZawartosc = zawartosc.replace("kota","psa")
print(nowaZawartosc)
plik.write(nowaZawartosc)
plik.close()
