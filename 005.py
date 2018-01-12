"""
#### Warsztat: Kostka do gry

W grach planszowych i papierowych RPG używa się wielu rodzajów kostek do gry,
nie tylko tych dobrze znanych, sześciennych. Jedną z popularniejszych kości jest np.
kostka dziesięciościenna, a nawet stuścienna! Jako że w grach kośćmi rzuca się często, pisanie za każdym razem np. _"rzuć dwiema kostkami dziesięciościennymi, a do wyniku dodaj 20"_ byłoby nudne, trudne i marnowałoby ogromne ilości papieru. W takich sytuacjach używa się kodu _"rzuć 2D10+20"_.

Kod takiej kostki wygląda następująco:

### xDy+z

gdzie:
* __y__ &ndash; rodzaj kostek, których należy użyć (np. D6, D10),
* __x__ &ndash; liczba rzutów kośćmi; jeśli rzucamy raz, ten parametr jest pomijalny,
* __z__ &ndash; liczba, którą należy dodać (lub odjąć) do wyniku rzutów (opcjonalnie).

__Przykłady:__

* __2D10+10__: 2 rzuty D10, do wyniku dodaj 10,
* __D6__: zwykły rzut kostką sześcienną,
* __2D3__: rzut dwiema kostkami trójściennymi,
* __D12-1__: rzut kością D12, od wyniku odejmij 1.

Napisz funkcję, która:

* przyjmie w parametrze taki kod w postaci stringa,
* rozpozna wszystkie dane wejściowe:
    * rodzaj kostki,
    * liczbę rzutów,
    * modyfikator,
* wykona symulację rzutów i zwróci wynik.

Typy kostek występujące w grach: D3, D4, D6, D8, D10, D12, D20, D100.
"""
from random import randint

def dice_roller(roll):

    d_index = roll.index("D")
    if d_index == 0:
        x = 1
    else:
        x = int(roll[:d_index])

    if "+" in roll:
        plus_index = roll.index("+")
        y = int(roll[d_index+1:plus_index])
        z = int(roll[plus_index+1:])
    elif "-" in roll:
        minus_index = roll.index("-")
        y = int(roll[d_index+1:minus_index])
        z = int(roll[minus_index+1:]) * -1
    else:
        y = int(roll[d_index+1:])
        z = 0

    print(x, y, z)
    return sum([randint(1, y) for i in range(x)]) + z



print(dice_roller("2D10+10"))
print(dice_roller("D6"))
print(dice_roller("D12-1"))
print(dice_roller("2D3"))

