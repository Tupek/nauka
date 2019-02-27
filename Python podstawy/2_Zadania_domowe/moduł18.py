from flask import Flask, request, render_template
from math import factorial
app = Flask(__name__)
@app.route("/", methods=["GET"])
def formatka():
    return render_template("n.html")

@app.route("/", methods=["POST"])    
def en():
    n = request.form["n"]
    n = int(n)
    linia = "-" * 30 + "<br/>"
    licz = 2 ** n
    licz = str(licz)
    licz2 = n ** n
    licz2 = str(licz2)
    licz3 = factorial(n)
    licz3 = str(licz3)
    
    wyslij = "Dwa do potęgi n: {} <br/>".format(licz)
    wyslij2 = "N do potegi n: {} <br/>".format(licz2)
    wyslij3 = "N silnia: {}".format(licz3)
    return wyslij + linia + wyslij2 + linia + wyslij3
    
if __name__ == "__main__":
    app.run(debug=True)
