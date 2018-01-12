from random import shuffle

lotto_nums = list(range(1, 50))
shuffle(lotto_nums)
lotto_nums = sorted(lotto_nums[:6])

user_guess = []
i = 1
while i < 7:
    try:
        x = int(input("Podaj liczbę nr %s " % i))
        if x not in range(1, 50):
            print("Liczba nie jest z zakresu 1-49")
        elif x in user_guess:
            print("Wytypowałeś już tę liczbę")
        else:
            user_guess.append(x)
            i += 1
    except ValueError:
        print("To nie jest liczba")

user_guess = sorted(user_guess)
print(user_guess)

guessed = len(set(user_guess) & set(lotto_nums))

if guessed > 2:
    print("Trafiłeś %s" % guessed)




