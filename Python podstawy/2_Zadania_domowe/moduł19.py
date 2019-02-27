from flask import Flask, request, render_template
app = Flask(__name__)
@app.route("/", methods=["GET"])
def formatka():
    return render_template("kod.html")

@app.route("/", methods=["POST"])
def kod():
    kod = request.form["kod"]
    if kod[2:3] == "-" and len(kod[0:2]) == 2 and len(kod) == 6:
        return "Kod jest poprawny"
    else:
        return "Kod jest niepoprawny"
        
if __name__ == "__main__":
    app.run(debug=True)
