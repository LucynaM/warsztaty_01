"""
#### Warsztat: Gra w zgadywanie liczb.

Napisz prostą grę w zgadywanie liczb. Komputer musi wylosować liczbę w zakresie 1 &ndash; 100. Następnie:

1. Zadać pytanie: "Zgadnij liczbę" i pobrać liczbę z klawiatury.
2. Sprawdzić, czy wprowadzony napis, to rzeczywiście liczba i w razie błędu wyświetlić komunikat "To nie jest liczba", po czym wrócić do pkt. 1
3. Jeśli liczba podana przez użytkownika jest mniejsza niż wylosowana, wyświetlić komunikat "Za mało!", po czym wrócić do pkt. 1.
4. Jeśli liczba podana przez użytkownika jest większa niż wylosowana, wyświetlić komunikat "Za dużo!", po czym wrócić do pkt. 1.
5. Jeśli liczba podana przez użytkownika jest równa wylosowanej, wyświetlić komunikat "Zgadłeś!", po czym zakończyć działanie programu.
"""
from random import randint


while True:
    rnd = randint(1, 100)
    guessed = False
    while not guessed:
        try:
            user_num = int(input("Zgadnij liczbę: "))
            if user_num > rnd:
                print("Za dużo")
            elif user_num < rnd:
                print("Za mało")
            else:
                print("Zgadłeś")
                guessed = True
        except ValueError:
                print("To nie jest liczba")
    decision = input("Jeżeli chcesz skończyć kliknij q")
    if decision == "q":
        break
