# gra wisielec
#
# Gracz ma za zadanie odgadnac losowy wyraz zgadujac litery.
# jesli mu sie to nie uda, maly ludzik zostaje powieszny
# wyrazy nie zawieraja Polskich znakow
 
# import modulow
import random
 
# stałe
HANGMAN = (
"""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | 
 |   | 
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | |
 |   | |
 |  
----------
""")
 
MAX_WRONG = len(HANGMAN) - 1 # stala reprezentujaca max dlugosc prob 7
WORDS = ("kolek", "wisielec", "system", "kalkulator", "telefon", "zabawka")
 
#inicjalizacja zmiennych
word = random.choice(WORDS) # losowe generowany wyraz z listy
so_far = "*" * len(word)    # * reprezentuje nie odgadniete litery
wrong = 0                   # zmienna rejestruje liczbe prob
used = []                   # zmienna zawierajaca litery zgadywne, uzyte
 
print("Witam Cie w grze 'Wisielec'.")
print("Zasady sa proste, musisz odgadnac wyraz, inaczej zostaniesz powieszony. Powodzenia")
print(word)      
 
while wrong < MAX_WRONG and so_far != word: # wykonuje sie tak dlugo az nie przekroczyli limit prob lub nie odgadniemy wyrazu
    print(HANGMAN[wrong])                  
    print("\nUzyles juz nastepujacych liter: \n", used) 
    print("\nSlowo, ktore szukasz na razie wyglada tak: \n", so_far) 
 
    guess = input("\nPodaj litere: ")# zmienna sterujaca petla
    guess = guess.lower()            # okreslam iz zawsze bedzie to mala litera
 
    while guess in used: # petla sprawdzajaca czy litera nie jest ponownie uzywana
        print("Uzyles juz tej litery, wprowadz inna !!")
        guess = input("Podaj nowa litere: ")
        guess = guess.lower()
 
    used.append(guess) # dodajemy litere do naszej zmiennej
 
    if guess in word:
        print("\nTak twoja litera", guess, " wystepuje w szukanym wyrazie")
 
        new = "" # datkowa zmienna to wyswietlania odgadnietych juz liter
        for i in range(len(word)): # petla do wyswietlania liter
            if guess == word[i]:   # sprawdzanie czy litera jest w wyrazie literujac go
               new += guess        # tworzy lancuch z liter ktore wystepuja w szykanym wyrazie
            else:                  # nastepnie zapisuje odgadniete juz litery
               new += so_far[i]    
        so_far = new
    else:    # dopisywanie ilosci przerzejsc petli
        print("\n Niestety litera: ",guess, " nie wystepuje w wyrazie")
        wrong += 1
 
if wrong == MAX_WRONG:  # jesli ilosc przejsc jest rowna 8 zatrzymuje
    print(HANGMAN[wrong])
    print("\n zostales powieszony!")
    print("\nszukany wyraz to ",word)
else:                   
    print("gratuluje, odgadnoles wyraz")
 
 
 
input("\nAby zakonczyc program, nacisnij klawisz Enter.")
