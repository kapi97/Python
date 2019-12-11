import winsound

tytul = input("Podaj nazwe pliku do odtworzenia: ")

winsound.PlaySound(tytul, winsound.SND_FILENAME)
