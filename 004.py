"""

Zaimplementuj odwróconą grę w zgadywanie liczb w aplikacji webowej przy pomocy Flaska.
Użytkownik dostaje do dyspozycji formularz z trzema guzikami: **więcej**, **mniej**, **trafiłeś**.

Informacje o aktualnych zmiennych `min` i `max` przechowuj w ukrytych polach formularza (pole typu hidden).

Uwaga - nie jest to rozwiązanie bezpieczne, bo użytkownik może ręcznie zmienić tego htmla,
np. przy pomocy Firebuga. Ale w tej sytuacji zupełnie wystarczające, co najwyżej zepsuje sobie zabawę ;)
"""

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def guess_num(max=1000, min=0, guess=None):

    if request.method == "POST":
        answer = request.form["answer"]
        min = int(request.form["min"])
        max = int(request.form["max"])

        if answer == "start":
            guess = int((max - min) / 2 + min)
            return render_template("004.html", max=max, min=min, guess=guess)
        elif answer == "more":
            guess = int(request.form["guess"])
            min = guess
        elif answer == "less":
            guess = int(request.form["guess"])
            max = guess
        else:
            min = 0
            max = 1000
            return render_template("004.html", max=max, min=min, guess=guess)

        guess = int((max - min) / 2 + min)
        return render_template("004.html", max=max, min=min, guess=guess)


    return render_template("004.html", max=max, min=min, guess=guess)

if __name__ == "__main__":
    app.run(debug=True)