

print("Pomyśl liczbę od 0 do 1000, a ja ją zgadnę w max 10 ruchach")


min = 0
max = 1000
guessed = False

while not guessed:
    guess = int((max - min) / 2 + min)
    print("Zgaduję %s" % guess)
    answer_1 = input("zgadłem? (y or n) ")
    if answer_1 == "y":
        print("Wygrałem")
        guessed = True
    else:
        answer_2 = input("za dużo? (y or n) ")
        if answer_2 == "y":
            max = guess
        else:
            answer_3 = input("za mało? (y or n) ")
            if answer_3 == "y":
                min = guess
            else:
                print("Nie oszukuj")






